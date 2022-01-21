#include "TString.h"
#include "TChain.h"
#include "TH1D.h"
#include "TF1.h"
#include "TMath.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TTree.h"
#include <vector>
#include <map>
#include <fstream>

void makeInputDACPlot(){
    // rootfile name
    TString file_name_run009 = "/data/hamada/easiroc_data/run009.root";
    TString file_name_run010 = "/data/hamada/easiroc_data/run010.root";
    TString file_name_run011 = "/data/hamada/easiroc_data/run011.root";
    
    // open rootfile
    TChain *chain_run009 = new TChain("tree");
    TChain *chain_run010 = new TChain("tree");
    TChain *chain_run011 = new TChain("tree");
    chain_run009->Add(file_name_run009);
    chain_run010->Add(file_name_run010);
    chain_run011->Add(file_name_run011);
    chain_run009->SetBranchStatus("*", 0);
    chain_run010->SetBranchStatus("*", 0);
    chain_run011->SetBranchStatus("*", 0);
    chain_run009->SetBranchStatus("VadcHigh", 1);
    chain_run010->SetBranchStatus("VadcHigh", 1);
    chain_run011->SetBranchStatus("VadcHigh", 1);

    // runNo to HV
    std::map<Int_t, Double_t> runNotoHV;
    runNotoHV[009] = 52.86;
    rubNotoHV[010] = 52.72;
    runNotoHV[011] = 52.96;
    Double_t HV_run009 = runNotoHV[009];
    Double_t HV_run010 = runNotoHV[010];
    Double_t HV_run011 = runNotoHV[011];

    // define fit range map
    // HV, ch, fit_min, fit_max
    std::map<double, std::map<int, std::pair<double, double>>> fit_range = fitRange();

    // define histgram range
    Int_t X_MIN_run009 = 950;
    Int_t X_MAX_run009 = 3500;
    Int_t X_BIN_run009 = X_MAX - X_MIN;
    
    // define fit parameters vector
    std::vector<std::vector<std::pair<Double_t, Double_t>>> fit_MPV(64);

    // defint fill parameter
    Int_t N = 0;
    Int_t ADC_count = 0;
    Doublr_t HV = 0;
    Int_t X_MIN = 0;
    Int_t X_MAX = 0;
    Int_t X_BIN = 0;

    //make histgram and fitting
    for (k = 0; k < 3; k++){
        if (k = 0) {
            // run009
            HV = HV_run009;
            TChain *chain = new TChain("tree");
            chain->Add(file_name_run009);
            chain->SetBranchStatus("*", 0);
            chain->SetBranchStatus("VadcHigh", 1);
            Int_t VadcHigh[64] = {};
            chain->SetBranchAddress("VadcHigh", &VadcHigh);
            N = chain->GetEntries();
        }
        if (k = 1) {
            // run010
            HV = HV_run010;
            TChain *chain = new TChain("tree");
            chain->Add(file_name_run010);
            chain->SetBranchStatus("*", 0);
            chain->SetBranchStatus("VadcHigh", 1);
            Int_t VadcHigh[64] = {};
            chain->SetBranchAddress("VadcHigh", &VadcHigh);
            N = chain->GetEntries();
        }
        else {
            // run011
            HV = HV_run011;
            TChain *chain = new TChain("tree");
            chain->Add(file_name_run011);
            chain->SetBranchStatus("*", 0);
            chain->SetBranchStatus("VadcHigh", 1);
            Int_t VadcHigh[64] = {};
            chain->SetBranchAddress("VadcHigh", &VadcHigh);
            N = chain->GetEntries();
        }

        for (j = 0; j < 64; j++){
            X_MIN = fit_range[HV][j].first;
            X_MAX = fit_range[HV][j].second;
            X_BIN = X_MAX - X_MIN;

            TH1D *hist = new TH1D("hist", "ADC; ADC count; Entries", X_BIN, X_MIN, X_MAX);
            for(Int_t i = 0; i < N; i++){
                chain->GetEntry(i);
                ADC_count = VadcHigh[j];
                hist->Fill(ADC_count);
            }
            //　define landau fit
            Int_t fit_MIN = fit_range[HV_run009][i].first;
            Int_t fit_MAX = fit_range[HV_run009][i].second;
            TF1 *func = new TF1("func", "landau", fit_MIN, fit_MAX);

            // draw
            TCanvas *canvas = new TCanvas();
            hist->Draw();
            hist->Fit(func,"R");
            canvas->Draw();
            fit_MPV.at(i).push_back(make_pair(HV_run009, func->GetParameter(1)));

            delete hist;
        }
    }
}
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
#include <utility>

// defult run009 52.86 V

std::vector<std::vector<std::pair<Double_t, Double_t>>> makeHistFit(){

    // HV, ch, fit_min, fit_max
    std::map<double, std::map<int, std::vector<std::pair<int, int>>>> fit_range = fitRange();

    // deffine fit parameters vestor
    std::vector<std::vector<std::pair<Double_t, Double_t>>> fitMPV(64);

    std::map<double, TString> file_names = {
        {52.86, TString("/data/hamada/easiroc_data/run009.root")},
        {52.72, TString("/data/hamada/easiroc_data/run010.root")},
        {52.96, TString("/data/hamada/easiroc_data/run011.root")}
    };

    Double_t HV = 0;

    for (Int_t k = 0; k < 3; k++){
        if (k == 0) HV = 52.86;
        if (k == 1) HV = 52.72;
        else HV = 52.96;
        
        TString file_name = file_names[HV];

        TChain *chain = new TChain("tree");
        chain->Add(file_name);
        chain->SetBranchStatus("*", 0);
        chain->SetBranchStatus("VadcHigh", 1);
        Int_t VadcHigh[64] = {};
        chain->SetBranchAddress("VadcHigh", &VadcHigh);
        Int_t N = chain->GetEntries();

        //define canvas
        TCanvas *canvas = new TCanvas("canvas", "c", 1920*2, 1080*16);
        canvas->Divide(4, 16);
        
        for(Int_t i = 0; i < 64; i++){
            Int_t X_MIN = 950;
            Int_t X_MAX = 3500;
            Int_t X_BIN = X_MAX - X_MIN;
            canvas->cd(i+1);
            TH1D *hist = new TH1D("hist", Form("ch%d;ADC;event", i), X_BIN, X_MIN, X_MAX);

            for(Int_t j = 0; j < N; j++){
                // make hist
                chain->GetEntry(j);
                hist->Fill(VadcHigh[i]);
            }

            //　define landau fit
            Int_t fit_MIN = fit_range[HV][i].at(0).first;
            Int_t fit_MAX = fit_range[HV][i].at(0).second;
            TF1 *func = new TF1("func", "landau", fit_MIN, fit_MAX);

            // draw
            hist->Draw();
            hist->Fit(func,"R");
            fitMPV.at(i).push_back(std::make_pair(HV, func->GetParameter(1)));

            delete hist;
        }

        TString save_file_name = file_name.ReplaceAll(".root", "_fit.png");
        canvas->SaveAs(save_file_name);

        delete canvas;

    }
    // debug output
    std::cout << fitMPV.at(0).size() << std::endl;

    for(Int_t i = 0; i < fitMPV.size(); i++){
        for(Int_t j = 0; j < fitMPV.at(i).size(); j++){
            std::cout << fitMPV.at(i).at(j).first << std::endl;
            std::cout << fitMPV.at(i).at(j).second << std::endl;
        }
    }

    return fitMPV;

}
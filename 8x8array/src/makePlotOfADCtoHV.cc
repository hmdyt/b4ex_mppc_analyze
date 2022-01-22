#include "TMath.h"
#include "TString.h"
#include "TGraph.h"
#include "TString.h"
#include "TCanvas.h"
#include "TF1.h"
#include <vector>


void makePlotOfADCtoHV(){
    std::vector<std::vector<std::pair<Double_t, Double_t>>> fitMPV = makeHistFit();

    TCanvas *canvas = new TCanvas("canvas", "c", 1920*2, 1080*16);
    canvas->Divide(4, 16);

    // debug output
    std::cout << fitMPV.size() << std::endl;

    // set fit range
    Int_t FIT_MIN = 950;
    Int_t FIT_MAX = 3500;
    
    // i = ch
    for (Int_t i = 0; i < fitMPV.size(); i++){
        canvas->cd(i + 1);
        TGraph *g = new TGraph();
        TF1 *func = new TF1("func", "[0] * x + [1]", FIT_MIN, FIT_MAX); 
        for(Int_t j = 0; j < fitMPV.at(i).size(); j++){
            // y
            Double_t HV = fitMPV.at(i).at(j).first;
            // x
            Double_t MPV = fitMPV.at(i).at(j).second;
            g->SetPoint(j, MPV, HV);
            g->SetMarkerStyle(22);
            g->SetMarkerColor(2);
            g->SetMarkerSize(1);
        }
        g->Draw("AP");
        g->Fit(func, "R");
        //func->GetParameter(0)
    }
    TString save_filename = "/data/hamada/easiroc_data/plotOfADCtoHV.png";
    canvas->SaveAs(save_filename);
}
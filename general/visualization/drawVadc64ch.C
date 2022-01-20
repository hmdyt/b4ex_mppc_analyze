#include "TROOT.h"
#include "TFile.h"
#include "TH1D.h"
#include "TString.h"
#include "TCanvas.h"

void drawVadc64ch(TString filepath = "/data/hamada/easiroc_data/run008.root", int is_logY=1){
    gROOT->SetBatch();
    TFile* file = new TFile(filepath, "read");
    TCanvas* canvas = new TCanvas("c", "c", 1920*2, 1080*16);
    canvas->Divide(4, 16);

    for (int i = 0; i < 64; i++) {
        canvas->cd(i+1);
        TH1D* hist = (TH1D*) file->Get(Form("ADC_HIGH_%d", i));
        hist->Draw();
        gPad->SetLogy(is_logY);
    }

    TString save_file_name = filepath.ReplaceAll(".root", ".png");
    canvas->SaveAs(save_file_name);
}
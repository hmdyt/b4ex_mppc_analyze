#include "TString.h"
#include "TChain.h"
#include "TH1D.h"
#include "TF1.h"
#include "TGraph.h"
#include "TCanvas.h"
#include <iostream>
#include <fstream>
#include <utility>
#include <vector>
#include <map>

#define X_MIN 950
#define X_MAX 3500

class MuonCalibration
{
private:
    double _HV;
    TString _file_path;
    std::map<int, std::vector<std::pair<int, int>>> _landau_fit_range;
    TChain* _chain;
    TH1D* _hists[64];
    TF1* _f_landau[64];
    Int_t _current_ch;
    Int_t _VadcHigh[64] = {};


public:
    MuonCalibration(double HV, TString file_path);
    ~MuonCalibration();

public:
    void fit();
    void save_as(TString save_path);
    void save_64ch_as(TString save_path);

public:
    double getHV(){return _HV;}
    TString get_file_path(){return _file_path;}
    void set_ch(Int_t ch){_current_ch = ch;}
    Int_t get_ch(){return _current_ch;}
    TH1D* get_hist(){return _hists[_current_ch];}
    TF1* get_f_landau(){return _f_landau[_current_ch];}
};

MuonCalibration::MuonCalibration(double HV, TString file_path)
{
    _HV = HV;
    _file_path = file_path;
    std::map<double, std::map<int, std::vector<std::pair<int, int>>>> tmp = fitRange();
    _landau_fit_range = tmp[_HV];
    _chain = new TChain("tree");
    _chain->Add(_file_path);
    _chain->SetBranchAddress("VadcHigh", &_VadcHigh);
}

MuonCalibration::~MuonCalibration()
{
}

void MuonCalibration::fit(){
    Int_t fit_MIN = _landau_fit_range[_current_ch].at(0).first;
    Int_t fit_MAX = _landau_fit_range[_current_ch].at(0).second;
    _hists[_current_ch] = new TH1D(
        Form("hist%d", _current_ch),
        Form("%s %f ch%d;ADC value;Events", _file_path.Data(), _HV, _current_ch),
        X_MAX - X_MIN, X_MIN, X_MAX
    );
    _f_landau[_current_ch] = new TF1(
        Form("f_landau%d", _current_ch),
        "landau",
        fit_MIN,
        fit_MAX
    );
    
    for (Int_t i_event = 0; i_event < _chain->GetEntries(); i_event++){
        _chain->GetEntry(i_event);
        _hists[_current_ch]->Fill(_VadcHigh[_current_ch]);
    }
    if (fit_MIN == 0 || fit_MAX == 0){
        _f_landau[_current_ch]->SetParameters(0, 0, 0);
    } else {
        _hists[_current_ch]->Fit(_f_landau[_current_ch], "R");
    }

}

void MuonCalibration::save_as(TString save_path){
    TCanvas* c = new TCanvas();
    c->cd();
    _hists[_current_ch]->Draw();
    c->SaveAs(save_path);
}

void MuonCalibration::save_64ch_as(TString save_path){
    TCanvas *canvas = new TCanvas("canvas", "c", 1920*2, 1080*16);
    canvas->Divide(4, 16);
    for (Int_t ch = 0; ch < 64; ch++){
        canvas->cd(ch+1);
        _hists[ch]->Draw();
    }
    canvas->SaveAs(save_path);
}

TGraph* drawHVvsADC(Int_t ch = 0){
    MuonCalibration* m[3] = {
        new MuonCalibration(52.86, TString("/data/hamada/easiroc_data/run009.root")),
        new MuonCalibration(52.72, TString("/data/hamada/easiroc_data/run010.root")),
        new MuonCalibration(52.96, TString("/data/hamada/easiroc_data/run011.root"))
    };
    std::vector<double> HVs;
    std::vector<double> MPVs;
    for (Int_t i = 0; i < 3; i++){
        m[i]->set_ch(ch);
        m[i]->fit();
        if (m[i]->get_f_landau()->GetParameter(1) == 0){ continue; }
        MPVs.push_back(m[i]->get_f_landau()->GetParameter(1));
        HVs.push_back(m[i]->getHV());
    }
    TGraph* g = new TGraph(MPVs.size(), &HVs[0], &MPVs[0]);
    g->SetMarkerStyle(8);
    g->SetTitle(Form("ch%d;HV;ADC value", ch));
    return g;
}

void test01(Int_t ch = 0){
    MuonCalibration* m[3] = {
        new MuonCalibration(52.86, TString("/data/hamada/easiroc_data/run009.root")),
        new MuonCalibration(52.72, TString("/data/hamada/easiroc_data/run010.root")),
        new MuonCalibration(52.96, TString("/data/hamada/easiroc_data/run011.root"))
    };
    std::vector<double> HVs;
    std::vector<double> MPVs;
    for (Int_t i = 0; i < 3; i++){
        m[i]->set_ch(ch);
        m[i]->fit();
        if (m[i]->get_f_landau()->GetParameter(1) == 0){ continue; }
        MPVs.push_back(m[i]->get_f_landau()->GetParameter(1));
        HVs.push_back(m[i]->getHV());
    }
    TGraph* g = new TGraph(MPVs.size(), &HVs[0], &MPVs[0]);
    g->SetMarkerStyle(8);
    g->SetTitle(Form("ch%d;HV;ADC value", ch));
    
    TCanvas* canvas = new TCanvas("canvas", "c", 1920/2, 1080);
    canvas->Divide(2, 2);
    canvas->cd(1);
    g->Draw("AP");
    canvas->cd(2);
    m[0]->get_hist()->Draw();
    canvas->cd(3);
    m[1]->get_hist()->Draw();
    canvas->cd(4);
    m[2]->get_hist()->Draw();
    canvas->Draw();
}

void fitMuonCalibration(){
    MuonCalibration* m[3] = {
        new MuonCalibration(52.86, TString("/data/hamada/easiroc_data/run009.root")),
        new MuonCalibration(52.72, TString("/data/hamada/easiroc_data/run010.root")),
        new MuonCalibration(52.96, TString("/data/hamada/easiroc_data/run011.root"))
    };
    
    TCanvas *canvas = new TCanvas("canvas", "c", 1920*2, 1080*16);
    canvas->Divide(4, 16);
    std::ofstream ofs("HV_ADC_pol1_list", std::ios::out);
    ofs << "#ch a b" << std::endl;
    TF1* f_pol1s[64];
    TGraph* graphs[64];
    for (Int_t ch = 0; ch < 64; ch++){
        canvas->cd(ch+1);
        graphs[ch] = drawHVvsADC(ch);
        f_pol1s[ch] = new TF1(Form("pol1 ch%d", ch), "[0]*x+[1]", 0, 60);
        graphs[ch]->Fit(f_pol1s[ch], "R");
        graphs[ch]->Draw("AP");
        ofs << ch << " ";
        ofs << f_pol1s[ch]->GetParameter(0) << " ";
        ofs << f_pol1s[ch]->GetParameter(1) << " ";
        ofs << std::endl;
    }
    canvas->SaveAs("HV_ADC_plot_muon_calb.png");
    
}

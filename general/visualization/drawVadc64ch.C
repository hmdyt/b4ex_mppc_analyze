void drawVadc64ch(
    TString file_path = "/data/hamada/easiroc_data/test_20211126_6_*.root",
    bool save_current_dir = false
    ){
    TChain* chain = new TChain("tree");
    chain->Add(file_path);

    TCanvas* canvas = new TCanvas("c", "c", 1920*2, 1080*16);
    canvas->Divide(4, 16);

    for (Int_t i = 0; i < 64; i++){
        canvas->cd(i+1);
        chain->Draw(Form("VadcHigh[%d]", i));
    }

    TString save_file_name;
    if (save_current_dir){
        // file_path = "/data/hamada/easiroc_data/test_20211126_5_*.root"
        // => save_file_name = "test_20211126_5_*.png"
        save_file_name = ((TString) file_path(file_path.Last('/')+1, file_path.Length())).ReplaceAll(".root", ".png");
    } else {
        save_file_name = file_path.ReplaceAll(".root", ".png");
    }
    canvas->SaveAs(save_file_name);
}
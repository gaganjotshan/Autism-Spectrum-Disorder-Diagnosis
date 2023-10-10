## 1. Install CPAC
If you have Docker, try directly:
__(REQUIRES PYTHON 3.6+)__
```
pip install cpac
cpac pull
```

if it doesn't work install singularity:
--> https://github.com/sylabs/singularity/releases/tag/v3.9.2 to download from source
or if you have __brew__:
```
brew install singularity
```

and try again to pull (`cpac pull`)

## 2. Prepare the data
The following commands assume that you have as working directory your Downloads folder, and that the directory containing the image files (call it `brain_img_data`) has the structure:
```
Anatomical Template:  ~/Downloads/brain_img_data/{site}/{participant}/{session}/anat_*/anat.nii.gz
Functional Template:  ~/Downloads/brain_img_data/{site}/{participant}/{session}/rest_*/rest.nii.gz
```

If not you will need to modify the yaml files and the bash commands accordingly.

Take the `subj_list2.txt`, `pipeline_singularity.yml` and the `data_settings.yml` files and place them in the Downloads folder as well.

### 2.1. Modify `data_settings.yml`:
replace for every path the '~' with your absolute path to the Downloads folder (for example `/Users/yourname/Downloads/...`)

### 2.2. Create data config file
Execute:
```
cd ~/Downloads
singularity run -B ~/Downloads -B ~/Downloads/brain_img_data C-PAC.sif ~/Downloads/brain_img_data ~/Downloads cli -- utils data_config build data_settings.yml 
```

this will create a file called `data_config.yml` in Downloads.

Modify the `data_config.yml`:
check if there are subjects with no `func` entry and remove them.
For example:
```
- anat: /home/nap-smasher/Downloads/brain_img_data/28680/session_1/anat_3/anat.nii.gz
  func:
    func-1:
      scan: /home/nap-smasher/Downloads/brain_img_data/28680/session_1/rest_1/rest.nii.gz
  site: site-1
  subject_id: '28680'
  unique_id: session_1
- anat: /home/nap-smasher/Downloads/brain_img_data/28682/session_2/anat_3/anat.nii.gz
  site: site-1
  subject_id: '28682'
  unique_id: session_2
- anat: /home/nap-smasher/Downloads/brain_img_data/28684/session_1/anat_3/anat.nii.gz
  func:
    func-1:
      scan: /home/nap-smasher/Downloads/brain_img_data/28684/session_1/rest_2/rest.nii.gz
  site: site-1
  subject_id: '28684'
  unique_id: session_1
```
here you can see that subject 28682 doesn't have the fMRI file, so it must be removed:
```
- anat: /home/nap-smasher/Downloads/brain_img_data/28680/session_1/anat_3/anat.nii.gz
  func:
    func-1:
      scan: /home/nap-smasher/Downloads/brain_img_data/28680/session_1/rest_1/rest.nii.gz
  site: site-1
  subject_id: '28680'
  unique_id: session_1
- anat: /home/nap-smasher/Downloads/brain_img_data/28684/session_1/anat_3/anat.nii.gz
  func:
    func-1:
      scan: /home/nap-smasher/Downloads/brain_img_data/28684/session_1/rest_2/rest.nii.gz
  site: site-1
  subject_id: '28684'
  unique_id: session_1
```

## 3. Run preprocessing
```
cpac run brain_img_data/ brain_data_processed/ --skip_bids_validator participant --pipeline_file pipeline_singularity.yml --data_config_file data_config.yml 
```
The results will be saved in the `brain_data_processed` folder
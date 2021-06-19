
## Wildfire affected lake color and productivity
[![DOI](https://zenodo.org/badge/361258764.svg)](https://zenodo.org/badge/latestdoi/361258764)


This repository uses chebysev center points of lakes in the HydroLakes database and matches them with Monitoring Trends in Burn Severity (MTBS) fire perimeters and AquaSat in-situ data to analyze lake color and productivity in response to fire.

### Project goals:
    
   * Match buffered lake center points with MTBS burn perimeters in Colorado, USA
   * Merge burned CO lakes with LimnoSat and AquaSat datasets to review changes in reflectance values and chlorophyll a concentrations in response to fire
   * Characterize lake catchments and affecting fires
   * Perform analysis to determine the relative influence of fire and catchment characteristics on chlorphyll and lake color. 
    
### Motivation and contribution:
    
   Severe wildfire kills vegetation and burns soil which increases transport of nutrients to streams and lakes. 
Increased transport can result in harmful algal blooms and diminished water treatability. Many communities in the US Southwest, 
including the Colorado Front Range, rely on forested montane watersheds for clean drinking water. The ability to 
remotely identify the characteristics within a watershed that are correlated to increased algal production will allow 
for more effective predictions about the effect of wildfire on water supply and support proactive and cost-effective 
mitigation efforts by civic leaders in the event their water supply is affected by fire. This workflow utilizes several 
large datasets to characterize pre- and post-fire landscapes to understand the drivers of lake responses to fire.

### Setup:
    
   Required packages are found in the repository .yml. To set up this repository, you will need to:
   1. Create the conda envrironment included in the repository
   2. Install datatools package with 'pip install -e .'
   3. Run desired notebooks in Jupyter
   
#### Conda Environment setup
    
  1. In bash, `cd` to the `ea-2021-final-project-wildfire_lake_productivity` repo
  2. Install the environment file
  3. Activate the environment
  4. Install supporting functions found in the 'datatools' package

```
$ cd ea-2021-final-project-wildfire_lake_productivity
$ conda env create -f environment.yml
$ conda activate wildfire-lake-productivity
$ pip install -e .
$ jupyter notebook

```
#### Data Collection  and analysis 

Notebooks containing Python script required to collect, review, and analyze data are contained in the "data_collection_and_analysis_notebooks" directory and numbered according to workflow beginning with "01_download_clip_merge".  All datasets can be imported via url and clipped to an area of interest, though script to save clipped datasets locally may be used to avoid repeated downloads. Scripts after "01_download_clip_merge" may call these stored clipped and merged datasets for visualization and analysis. Updated project progress may be found in the 'blog_post.ipynb' notebook.

### Maintainers:
Lauren Kremer, 
Research Associate, 
Watershed Research Group at Colorado State University
![Lauren Kremer](https://avatars.githubusercontent.com/u/70210769?v=4)
     
### Contributors:
[Matthew V. Ross, PhD](https://matthewrvross.com)
Assistant Professor of Water Quality, Colorado State University

### Supporting Datasets:

#### AquaSat:
Ross, M. R. V., S. N. Topp, A. P. Appling, X. Yang, C. Kuhn, D. Butman, M. Simard, and T. M. Pavelsky. 2019. AquaSat: A Data Set to Enable Remote Sensing of Water Quality for Inland Waters. Water Resources Research 55:10012-10025.
[DOI: 10.1029/2019WR024883](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019WR024883)

#### LimnoSat:
Topp, A. P., T. M. Pavelsky, H. A. Dugan, X. Yang, J. Gradner, M. R. V. Ross. 2021. Shifting Patterns of Summer Lake Color Phenology in Over 26,000 US Lakes. Water Resources Research 57:e2020WR029123.
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4139695.svg)](https://doi.org/10.5281/zenodo.4139695)

### License   

[BSD-3](https://github.com/earthlab/earthpy/blob/main/LICENSE)


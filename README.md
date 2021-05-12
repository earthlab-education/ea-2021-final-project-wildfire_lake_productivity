
## Wildfire affected lake color and productivity

This repository uses chebysev center points of lakes in the HydroLakes database and matches them with Monitoring Trends in Burn Severity (MTBS) fire perimeters and AquaSat in-situ data to analyze spatial and temporal pre- and post-wildfire trends in lake color.

### Project goals:
    
    * Match buffered lake center points with MTBS burn perimeters in Colorado, USA
    * Merge burned CO lakes with LimnoSat and AquaSat datasets to review changes in reflectance values and chlorophyll a concentrations in response to fire
    * Characterize lake catchments and affecting fires
    * Perform analysis to determine the relative influence of fire and catchment characteristics on chlorphyll and lake color. 
    
### Motivation and contribution:
    
    Severe wildfire kills vegetation and burns soil which increases transport of nutrients to streams and lakes. 
This can result in harmful algal blooms and diminished water treatability. Many communities in the US Southwest, 
including the Colorado Front Range, rely on forested montane watersheds for clean drinking water. The ability to 
remotely identify the characteristics within a watershed that are correlated to increased algal production will allow 
for more effective predictions about the effect of wildfire on water supply and support proactive and cost-effective 
mitigation efforts by civic leaders in the event their water supply is affected by fire. This workflow utilizes several 
large datasets to retroactively characterize landscapes to understand the drivers of lake responses to fire.

### Running the workflow:
    
     Required packages are found in the repository .yml. Notebooks containing Python script required to collect, review, and analyze data are contained in the "scripts" directory and numbered according to workflow beginning with "01_download_clip_merge".  All datasets can be imported via url and clipped to an area of interest, though script to save large, clipped datasets locally may be used to avoid repeated downloads. Scripts after "01_download_clip_merge" may call these stored clipped and merged datasets for visualization and analysis. Updated project progress may be found in the 'blog_post.ipynb' notebook.

### Maintainers:
![Lauren Kremer](https://avatars.githubusercontent.com/u/70210769?v=4)
     
### Contributors:
[Dr. Matthew V. Ross](https://matthewrvross.com)

### License & Citation    

[BSD-3](https://github.com/earthlab/earthpy/blob/main/LICENSE)


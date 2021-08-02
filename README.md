```
     ██████╗ ███████╗ ██████╗         ██████╗ ██╗██████╗ ███████╗██╗     ██╗███╗   ██╗███████╗
    ██╔════╝ ██╔════╝██╔═══██╗        ██╔══██╗██║██╔══██╗██╔════╝██║     ██║████╗  ██║██╔════╝
    ██║  ███╗█████╗  ██║   ██║        ██████╔╝██║██████╔╝█████╗  ██║     ██║██╔██╗ ██║█████╗  
    ██║   ██║██╔══╝  ██║   ██║        ██╔═══╝ ██║██╔═══╝ ██╔══╝  ██║     ██║██║╚██╗██║██╔══╝  
    ╚██████╔╝███████╗╚██████╔╝███████╗██║     ██║██║     ███████╗███████╗██║██║ ╚████║███████╗
     ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                          
                                        Developed by Ana Ausek
                                                Summer 2021
```

### Demo

<p align="center">
  <img src="gif.gif"/>
</p>

### Application Description

Custom NCBI GEO data download pipeline to assist in the analysis of GSE sample files.

### Installation Options
- To install GEO_Pipeline use `pip install geo-pipeline` then run `pipeline` to launch

- For a local install, `git clone` this repository
- Execute `python3 src/pipeline.py`
- `cd output/` for sample and metadata output files

### Links
- [Repository](https://github.com/aausek/GEO_Pipeline)
- [PIP Package](https://pypi.org/project/geo-pipeline/)

### Completed Features

- Prompt user for input to tailor NCBI query
- Query output results in a single .txt file with all associated samples
- Split consolidated output into individual sample files
- Recreate code in HiperGator cluster
- Identifying series platform ID for probe matching

### Pending Features

- Pair probe IDs with manufacturer's product data to identify gene

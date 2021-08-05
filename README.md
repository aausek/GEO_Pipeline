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

#### PIP install in current directory
- To install GEO_Pipeline in current directory use `pip install geo-pipeline -t .` 
- `cd src/` and run `python3 pipeline.py` to launch
- `output/` files will be deposited in `cd src/`

#### Cloning repository
- Alternatively, `git clone` this repository
- Execute `python3 src/pipeline.py`
- `cd output/` for sample and metadata output files

### Links
- [Repository](https://github.com/aausek/GEO_Pipeline)
- [PIP Package](https://pypi.org/project/geo-pipeline/)
- [Research Paper](https://www.overleaf.com/project/60df15e58e1c91216ea51895)

### Completed Features

- Prompt user for input to tailor NCBI query
- Query output results in a single .txt file with all associated samples
- Split consolidated output into individual sample files
- Download associated platform (GPL) files
- Convert all .txt data into JSON files
- Identifying series platform ID for probe matching

### Pending Features

- Pair probe IDs with manufacturer's product data to identify gene
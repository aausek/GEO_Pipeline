# GEO_Pipeline

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


### Completed Features

- Prompt user for input to tailor NCBI query
- Query output results in a single .txt file with all associated samples
- Split consolidated output into individual sample files
- Recreate code in HiperGator cluster
- Identifying series platform ID for probe matching

### Pending Features

- Pair probe IDs with manufacturer's product data to identify gene

### PIP Packaging

- In local directory edit `pipeline.py` and `setup.py` with new package version
- To create packaging files run `python3 setup.py sdist bdist_wheel` and `twine upload dist/*`
- New package will be uploaded to [PyPi](https://pypi.org/project/geo-pipeline/)
- To install run `pip install geo-pipeline` and `pipeline` to launch
# Multi-objective Bayesian Optimization for process optimization of L-PBF


## Case study

In this study, we employed the Multi-objective Bayesian Optimization algorithm called [DGEMO](https://github.com/yunshengtian/DGEMO) to predict the properties of a material (SS 316L) based on process conditions and provide recommendations for the next set of parameters that would yield denser and harder samples.

The metallic samples were fabricated in the additive manufacturing laboratory at Skoltech, Moscow. Each sample was produced using a specific set of process conditions, resulting in varying levels of hardness and porosity. The objective of our algorithm is to establish a mapping between the process conditions and the mechanical properties of the fabricated metallic parts. This mapping enables us to suggest novel process conditions that have not been explored before.

By leveraging the power of DGEMO, we aim to optimize the additive manufacturing process for SS 316L, ultimately improving the density and hardness of the printed samples. This optimization process can lead to enhanced material performance and open up new possibilities for advanced manufacturing applications.

## Citation

If you find our work helpful to your research, please consider citing our [paper](https://doi.org/10.3390/ma16031050).

```

@Article{ma16031050,
AUTHOR = {Chepiga, Timur and Zhilyaev, Petr and Ryabov, Alexander and Simonov, Alexey P. and Dubinin, Oleg N. and Firsov, Denis G. and Kuzminova, Yulia O. and Evlashin, Stanislav A.},
TITLE = {Process Parameter Selection for Production of Stainless Steel 316L Using Efficient Multi-Objective Bayesian Optimization Algorithm},
JOURNAL = {Materials},
VOLUME = {16},
YEAR = {2023},
NUMBER = {3},
ARTICLE-NUMBER = {1050},
URL = {https://www.mdpi.com/1996-1944/16/3/1050},
PubMedID = {36770057},
ISSN = {1996-1944},
ABSTRACT = {Additive manufacturing is a modern technique to produce parts with a complex geometry. However, the choice of the printing parameters is a time-consuming and costly process. In this study, the parameter optimization for the laser powder bed fusion process was investigated. Using state-of-the art multi-objective Bayesian optimization, the set of the most-promising process parameters (laser power, scanning speed, hatch distance, etc.), which would yield parts with the desired hardness and porosity, was established. The Gaussian process surrogate model was built on 57 empirical data points, and through efficient sampling in the design space, we were able to obtain three points in the Pareto front in just over six iterations. The produced parts had a hardness ranging from 224&ndash;235 HV and a porosity in the range of 0.2&ndash;0.37%. The trained model recommended using the following parameters for high-quality parts: 58 W, 257 mm/s, 45 &micro;m, with a scan rotation angle of 131 degrees. The proposed methodology greatly reduces the number of experiments, thus saving time and resources. The candidate process parameters prescribed by the model were experimentally validated and tested.},
DOI = {10.3390/ma16031050}
}
```




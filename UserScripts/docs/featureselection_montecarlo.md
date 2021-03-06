DESCRIPTION

    This command will execute each specified algorithm using a Monte Carlo cross-validation strategy. It will perform feature selection but not classification. It will output a ranked list of features for each algorithm as well as a Borda Count ranked list of features based on the rankings of all feature-selection algorithms.

REQUIRED ARGUMENTS

    --data [file_path]
    --description [description]
    --iterations [integer]
    --fs-algo [file_path]
    --output-dir [dir_path]

OPTIONAL ARGUMENTS

    --verbose [false|true]
    --seed [integer]
    --train-proportion [float]
    --ohe [false|true]
    --scale [none|standard|robust|minmax|maxabs|power|quantnorm|quantunif|normalizer]
    --impute [false|true]
    --num-cores [integer]
    --temp-dir [dir_path]

EXAMPLE

    UserScripts/nestedboth_montecarlo \
      --data Data.tsv.gz \
      --description "My_Interesting_Analysis" \
      --iterations 1 \
      --fs-algo "AlgorithmScripts/FeatureSelection/tsv/sklearn/anova/default" \
      --seed 33 \
      --scale robust \
      --output-dir Output/

NOTES

    The --data argument allows you to specify input data files in one of the supported formats (see https://github.com/srp33/ShinyLearner/blob/master/InputFormats.md).

    The --description value should be a user-friendly description of the analysis that will be performed. This description will be specified in the output files. If the description contains space characters, be sure to surround it in quotations.

    The --fs-algo argument allows you to specify feature-selection algorithm(s) to be used in the analysis. The value(s) should be a relative path to a script specified under AlgorithmScripts (for example, AlgorithmScripts/FeatureSelection/tsv/sklearn/anova). Alternatively, you may specify the name of a text file that ends with ".list" and contains a list of algorithms (one per line) that you would like to include in the analysis. See https://github.com/srp33/ShinyLearner/blob/master/Algorithms.md for more information about algorithms. This argument may be specified multiple times. Wildcards may be used (in quotes).

    The --data and --fs-algo arguments must be used at least once but can be used multiple times. Wildcards may be used (in quotations).

    The --iterations value must be a positive integer. It indicates the number of times that a round of cross-validation should be performed.

    The --output-dir argument allows you to indicate where output files will be stored. If this directory does not already exist, ShinyLearner will create it. For information about the output files that will be created, see https://github.com/srp33/ShinyLearner/blob/master/OutputFiles.md.

    The --verbose argument is set to false by default. If set to true, detailed information about the processing steps will be printed to standard out. This flag is typically used for debugging purposes.

    The --seed argument allows the user to specify a random seed for assigning samples to training and test set(s). This value is 1 by default.

    The --train-proportion argument allows the user to control the proportion of samples that are assigned (randomly) to each training set. The remaining samples are assigned to the corresponding test sets. By default, this value is 0.67. Valid values range between 0.1 and 0.9.

    The --ohe argument is set to true by default. This means that any categorical variables will be [one-hot encoded](https://www.quora.com/What-is-one-hot-encoding-and-when-is-it-used-in-data-science).
    
    The --scale argument is set to none by default (no scaling is performed). When set to one of the other options, any continuous variable(s) will be scaled using the specified method. Information about the scaling methods can be found on the [scikit-learn site](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py). Continuous variables will be scaled only if more than 50% of values are unique.

    The --impute argument is set to false by default. When set to true, missing values will be imputed. Median-based imputation will be used for continuous and integer variables. Mode-based imputation will be used for discrete variables. Any variable missing more than 50% of values across all samples will be removed. Subsequently, any sample missing more than 50% of values across all features will be removed. In input data files, missing values should be specified as ?, NA, or null.

    The --num-cores argument is set to 1 by default. When set to a number greater than 1, it will attempt to use multiple cores when executing a given algorithm. Not every algorithm supports parallelization.
    
    When a value is specified for --temp-dir, temporary files will be stored in the specified location; otherwise, temporary files will be stored in the operating system's default location for temporary files.

OUTPUTS

    SelectedFeatures.tsv

    SelectedFeatures_Summarized.tsv

    ElapsedTime.tsv

    Log.txt

    (Please see https://github.com/srp33/ShinyLearner/blob/master/OutputFiles.md for descriptions of what these files contain.)

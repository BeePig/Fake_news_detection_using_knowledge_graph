'''
=======================
Training an Algorithm
=======================
In this example, we will show how to import all the modules to start training and algorithm
'''
# Author: Sujit Rokka Chhetri
# License: MIT

import sys

from kg.utils.kgcontroller import KnowledgeGraph
from kg.config.config import Importer, KGEArgParser
from kg.utils.trainer import Trainer
from kg.example.data_process import create_data


def main():
    # getting the customized configurations from the command-line arguments.
    args = KGEArgParser().get_args(sys.argv[1:])
    args.dataset_name = "dbpedia"
    # Preparing data and cache the data for later usage
    knowledge_graph = KnowledgeGraph(dataset=args.dataset_name, custom_dataset_path=args.dataset_path)
    knowledge_graph.prepare_data()

    # Extracting the corresponding model config and definition from Importer().
    config_def, model_def = Importer().import_model_config(args.model_name.lower())
    config = config_def(args)
    model = model_def(config)

    # Create, Compile and Train the model. While training, several evaluation will be performed.
    trainer = Trainer(model=model)
    trainer.build_model()
    trainer.train_model()





if __name__ == "__main__":
    main()

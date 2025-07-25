import hydra
from omegaconf import DictConfig

@hydra.main(config_path="pkg://ldmlab/config", config_name="config", version_base=None)
def main(config: DictConfig):
    print(config)

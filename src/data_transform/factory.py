from .standard_scaler_transformer import StandardScalerTransformer
from .base_transformer import DataTransformer


class TransformerFactory:
    @staticmethod
    def get_transformer(method: str) -> DataTransformer:
        if method == "standard":
            return StandardScalerTransformer()
        raise ValueError(f"Unsupported transformation method: {method}")

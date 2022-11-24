import enum
from typing import List

import numpy as np
import pandas as pd
from sklearn import preprocessing as proc


class EncoderType(enum.Enum):
    """Encoder Enumeration type

    Args:
        enum (Enum): Inherits from python Enumeration
    """

    OneHot = 1
    Ordinal = 2
    Binary = 3
    Label = 4
    Cyclic = 5


class CatEncoder:
    """Encode Categorical columns"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.encoder = None

    @classmethod
    def lookup_encoder(cls, encoder_type: EncoderType):
        """Lookup Encoder mapping from enumeration to object type

        Args:
            encoder_type (EncoderType): _description_

        Returns:
           Calalble: Instance
        """
        encoder_types = {
            EncoderType.Label: proc.LabelEncoder,
            EncoderType.Binary: proc.LabelBinarizer,
            EncoderType.OneHot: proc.OneHotEncoder,
        }
        return encoder_types.get(encoder_type, EncoderType.Label)

    def fit_transform(
        self, df: pd.DataFrame, cat_features: List[str], encoder_type: EncoderType = EncoderType.Label
    ) -> pd.DataFrame:
        """Encode categorical information

        Args:
            df (pd.DataFrame): input dataframe
            cat_features (List[str]): categorical features to encode
            encoder_type (EncoderType, optional): type of encoder to choose from. Defaults to EncoderType.Label.

        Returns:
            pd.DataFrame: transformed column dataframe

        Examples:
        >>> enc = CatEncoder()
        >>> enc.fit_transform(df, 'name')
        >>> enc.encoder.classes_
        """
        # applicable for OHE for the matrix, where we can encode entire list of features
        self.encoder = CatEncoder.lookup_encoder(encoder_type)()
        self.encoder.fit(df[cat_features])
        return self.encoder.transform(df[cat_features].values)

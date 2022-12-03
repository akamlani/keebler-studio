import numpy as np
import tensorflow as tf


class PlattScaling(tf.keras.layers.Layer):
    """Modifies the raw logits of the modl, to be used for model calibration

    Requires a separate holdout dataset containing the emperical distribution to calibrate the layer

    Evaluation via comparing the average of model predictions against the rate observed in the system
    A calibration ration > 1 indicates overconfident predictions and visa versa
    A calibration ration < 1 indicates underconfident predictions and visa versa
    >>> calibration = engagement(yhat) / engaegment(emperical)
    """

    def __init__(self):
        super().__init__()
        self.a = self.add_weight(name="a", trainable=True, initialize=tf.keras.initializers.Ones())
        self.b = self.add_weight(name="b", trainable=True, initializer=tf.keras.initializers.Zeros())

    def call(self, logits: np.array, **kwargs) -> np.array:
        """_summary_

        Args:
            logits (np.array): predicted logits to calibrate on

        Returns:
            np.array: recalibration logits based on model calibration parameters
        """
        return self.a * logits + self.b

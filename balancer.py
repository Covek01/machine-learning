from imblearn.over_sampling import SMOTENC
from sklearn.utils import resample
from pandas import DataFrame
import ipdb


def balance_SMOTENC(
    df: DataFrame,
    feature_columns: list[str],
    target_column: str,
    categorical_features: list[int],
) -> DataFrame:
    """Performs SMOTE balancing on unbalanced dataframe per feature_column

    Args:
        df (DataFrame): entry DataFrame to balance
        feature_columns (list[str]): entry columns to perform SMOTE to
        target_column (str): target imbalanced column to perform SMOTE to

    Returns:
        DataFrame: balanced DataFrame
    """
    df_features = df[feature_columns]
    df_target = df[target_column]

    smote = SMOTENC(
        categorical_features=categorical_features,
        random_state=42,
    )
    X_resampled, y_resampled = smote.fit_resample(df_features, df_target)

    df_balanced = DataFrame(X_resampled, columns=feature_columns)
    df_balanced[target_column] = y_resampled

    return df_balanced


# def balance_upsample(df: DataFrame)

import dash_mantine_components as dmc

component = dmc.Select(
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    value="Pandas",
    clearable=True,
    w=200,
)

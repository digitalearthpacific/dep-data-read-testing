# Extent is over Numea, centered on -22.171638, 166.490348
EXTENT = [166, -23, 167, -22]
EXTENT_SMALL = [166.5, -22.5, 166.8, -22.2]
DATES = "2023-01"
LOAD_ARGS = dict(
    groupby="solar_day",
    chunks=dict(x=2048, y=2048),
)

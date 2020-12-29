import lookup_coordinates as la
import raw_location as rl

ADDR = [
    "Tagum Philippines",
    "Davao Philippines",
    "Isabela Philippines",
    "Surigao Philippines"
]

COORDINATES = rl(la(ADDR))


"""
Example of using TextAsset class.
"""
from ggame import TextAsset, Color

TA = TextAsset(
    "Sample Text", style="bold 40pt Arial", width=250, fill=Color(0x1122FF, 1.0)
)

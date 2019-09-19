#coding: utf-8
#PyScrach
#Author: Sheng Fan

# {
#     "extensionName": "FredTools Keys Detect",
#     "extensionPort": 13579,
#     "blockSpecs":[
#         ["r", "Shift Key", "key_shift"],
#         ["r", "Backspace Key", "key_backspace"],
#         ["r", "Ctrl Key", "key_ctrl"]
#     ]
# }

def CreateS2EFileContent(
        ExtName: str,
        ExtPort: int,
        BlockSpecs: str
):
    x = """{
    "extensionName": "%s",
    "extensionPort": %d,
    "blockSpecs":%s
}
""" % (ExtName, ExtPort, str(BlockSpecs))
    return x

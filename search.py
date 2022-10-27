# import os

from cgitb import lookup
from curses.ascii import islower
from os import walk
dir_path = r'/Users/rupinjairaj/projects/utd/sem3/forta-bot/bot_code'
# dir_path = r'/Users/rupinjairaj/projects/utd/sem3/forta-bot/bot_code/AE_Aave_Borrow_Collateral_Ratio_Monitor/app/src'
# # iterate each file in a directory
# for file in os.listdir(dir_path):
#     cur_path = os.path.join(dir_path, file)
#     # check if it is a file
#     if os.path.isfile(cur_path):
#         with open(cur_path, 'r') as file:
#             # read all content of a file and search string
#             if 'laptop' in file.read():
#                 print('string found')
#                 break

lookup_list = [
    "FortaConfig",
    "Initialize",
    "HandleTransaction",
    "HandleBlock",
    "Finding",
    "FindingSeverity",
    "FindingType",
    "BlockEvent",
    "TransactionEvent",
    "TxEventBlock",
    "Block",
    "Transaction",
    "Receipt",
    "Log",
    "LogDescription",
    "Trace",
    "TraceAction",
    "TraceResult",
    "EventType",
    "Network",
    "getJsonRpcUrl",
    "createTransactionEvent",
    "createBlockEvent",
    "getEthersProvider",
    "getEthersBatchProvider",
    "ethers",
    "keccak256",
    "setPrivateFindings",
    "isPrivateFindings",
    "configureContainer",
    "getTransactionReceipt",
    "getAlerts",
    "fetchJwt",
    "decodeJwt",
    "verifyJwt"
]


def generateTargetLines():
    result = []

    for (dirpath, dirnames, filenames) in walk(dir_path):
        # print(dirpath)
        for filename in filenames:
            if filename.endswith(".spec.js"):
                continue
            if filename.endswith(".js"):
                with open(dirpath + '/' + filename, 'r') as fp:
                    for l_no, line in enumerate(fp):
                        # search string
                        for element in lookup_list:
                            if islower(element[0]):
                                element = "." + element
                            else:
                                continue
                                element = element + "."
                            if element in line:
                                res = {
                                    'filename': dirpath+'/'+filename,
                                    'lineNumber': l_no,
                                    'line': line
                                }
                                result.append(res)
                                # print(
                                #     f"{element} found in file {dirpath}/{filename}")
                                # print('Line Number:', l_no)
                                # print('Line:', line)
    return result


print(generateTargetLines())

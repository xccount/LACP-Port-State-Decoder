import os
from tabulate import tabulate

print("LACP Actor Status Decoder", '\n')

clear = lambda: os.system('cls')

while True:
        print('')
        inpt = input("Type Port-State Code: ")
        if inpt == 'help':
                clear()
                print ('\n',tabulate([["LACP Activity", '0 - LACP mode Passive.'],
                                 ['', '1 - LACP mode Active.'],
                                ["LACP Timeout", '0 - LACP timeout is Short.'],
                                ['', '1 - LACP timeout is Long.'],
                                ["Aggregation", '0 - Link is NOT ready to be aggregated.'],
                                ['', '1 - Link is ready to be aggregated.'],
                                ["Synchronization", '0 - LACP frames are NOT in sync with partner.'],
                                ['', '1 - LACP frames are in sync with partner.'],
                                ["Collecting", '0 - Mux is Rejecting traffic received on this port.'],
                                ['', '1 - Accepting traffic received on this port.'],
                                ["Distributing", '0 - Mux is NOT sending traffic from this port.'],
                                ['', '1 - Mux is NOT sending traffic from this port.'],
                                ["Defaulted", '0 - Mux received parameters via LACP PDU.'],
                                ['', '1 - Mux is using admin defined parameters.'],
                                ["PDU Expired", '0 - is not in expired state.'],
                                ['', '1 - is in expired state.']],
                                headers=['FLAGS', 'STATES'], tablefmt="simple", colalign=("left",)),'\n\n*Mux - Multiplexer refers to the logical unit aggregates physical links into single logical unit.\n')
                continue
        
        if inpt:
                inpt_int = int(inpt, 16)
                inpt_bin = bin(inpt_int)
                inpt_bin = inpt_bin[2:].zfill(8)[::-1]

                #string to digit
                bin_arry = [int(x) for x in str(inpt_bin)]

                #variables
                if bin_arry[0] == 1:
                        LACP_Activity = "Active"
                else:
                    LACP_Activity = "Passive"

                if bin_arry[1] == 1:
                        LACP_Timeout = "Short Timeout"
                else:
                        LACP_Timeout = "Long Timeout"
                    
                if bin_arry[2] == 1:
                        Aggregation = "Yes"
                else:
                    Aggregation = "No (individual link)"
                    
                if bin_arry[3] == 1:
                        Synchronization = "In sync"
                else:
                    Synchronization = "NOT in sync"

                if bin_arry[4] == 1:
                        Collecting = "Mux is Collecting"
                else:
                    Collecting = "Mux is NOT Collecting"

                if bin_arry[5] == 1:
                        Distributing = "Mux is Distributing"
                else:
                    Distributing = "Mux is NOT Distributing"

                if bin_arry[6] == 1:
                        Defaulted = "Using Default PDU"
                else:
                    Defaulted = "via LACP PDU"

                if bin_arry[7] == 1:
                        Expired = "Yes"
                else:
                    Expired = "No"

                clear()
                print ('\n',str.upper(inpt),"=",inpt_bin, '(Hexadecimal converted to Binary and flipped)','\n')
                print (tabulate([[bin_arry[0], "LACP Activity", LACP_Activity],
                                [bin_arry[1], "LACP Timeout", LACP_Timeout],
                                [bin_arry[2], "Aggregation", Aggregation],
                                [bin_arry[3], "Synchronization", Synchronization],
                                [bin_arry[4], "Collecting", Collecting],
                                [bin_arry[5], "Distributing", Distributing],
                                [bin_arry[6], "Defaulted", Defaulted],
                                [bin_arry[7], "PDU Expired", Expired]],
                                headers=['Bit','FLAGS', 'STATE'], tablefmt="simple", colalign=("center",)))
                continue
        else:
                clear()
                print("> Type LACP Port-State hex code to decode.")
                print("> Type 'help' for the details.")
                print("> Press'ctrl+c' to close the application.", '\n')

def Composition(Text, k):
    retVal = []
    l = len(Text)
    for i in range(0,l-k+1):
        retVal.append(Text[i:i+k])
    return retVal

k = 5
Text = "CAATCCAAC"
k = 100
Text = "AGGGGGTCCCTTCTCGTGTATAACTTATTCGAAGGGGCAAAGGCGTTGAGCCACACACATTTTTCGGACTAAACTAGGCCCACGTAGGAAGGAGTGTTATTAGTTTGCTTTTTGTTGGGTCTGTAGCGTGGATACGGGTGATCCCAGCATCGATCACTTCGAGTCGTTTACACTAAGGATGTAGGTAAGAATTCCAAGCCTTGTTGAGTACTTCAGCTGTTGAGGATTACCAGGACAATAATTGTCTGCCCTCGACGTGAACGCGGTGCTGGAAGGTGGGGCTGTACTATTTCAGAAAAACGTTGTTAAATGGGGAACCATGGCCTTTCTAACTTATAAATATAGTGAATGGCCTACAGGCCGCCTGGAACTGTCGCATCCCGACCACATGTAGGGGAATCGTGTGTTGTGTTTTGCCGGGCGCTCAATGAGTTCGTGTGTCCCGTGCGCAATAGGTGGTATGGTGCGCTGACCGGTGGTATCTTCTCGAATTTACCCACCCTATACCGGTGAGGCCCTTGGGCTGTCTCGCAATACCTATTTCCAATAAAACTTAACGTCGCCCCCTCGAAAAGCTGAAGTATCCATGACATAGCCACTCACGCGTGAAAACGATCGAATCATCTGTCTCTTGCAGGTTGAGCGCAAGGATATATGTCAATTATTTTAGCCTATTGTATTCAAATTCCGGTGACGACAATTTTTTGTGGAGTGCACGGGGTTTAGATGTCAGTGAACGCGGCCAGGTGTAATAACCTGGTGGGGCCTTCCGGAATTGGCATACCTCAGTGACTGCCGTCTTTTTAATACCCACAATAGATCGGGTTTACTTGTCACAGGCAATCCCGATTGCGTAGCGTGGAGTTAAATTCTGCCCGGCGGTGTAATCCTCAACATCTTATGCCGAAACAATCATACATCACTCGAGACGGCCTCTGTCGCTGACACAATCCAATTTTGACATCCGAACTGGATTGGCCGCACACTAGTCTAGAAGAGTACGCGTTCCGCGGGGGTGACGATTTGATCCAAATGGAAAGTACTGACCGACTATAGAGGGCTCCCAGTTTACGGCTGTTTCCTATGTGATTAGCGGTGGTGGAGGAATCCTTGCACCTGCCTCGGAACCGCGTAGGGCTGTGTGGAAAACCCATGGAAATTATGATCTTCAGTCTTTAGTAACTCGCGTAGGTGCGGATGCGACGTTCGCGCACTTTATGTTTCATCGGGCTATGACTGATTTCCAACAGTCACAACCGAGGCTAGGGTTAAGAAGGGATACTGTAATAGTCATTTTGAGTGTGCTTGCTCGTCTCTGGCCCCGGGACGATACAATGTCTGACGACGGCGACGCGAGACCTAGCAGTATAAAACCCTGTCGTAACCCGGATGTTCTCCGTTCATATAGGAATCCTTTGCTTTCAATACCCTGGTAGAAGATCTCCGCATCTTTGAGCCTGTTTTTACCAGCATGGTGCTCAAAGCTCCGGAAAAAATCCCATAACCGGTATCCTACAAGAATGAAGCTTTGTAGGGCTCTAATACTGCACTCCTTCCAGTTGCACGGTTTTAGTTTCGTTCCAACCTAACCACCCTACCATCTATTCAATTTTAAATGCTACTGCCGGGTGCTAATACGGCGACCCTGAGGTGTTAGCATGTGACTGACCCCTTTTTTCTGTGAGTACCGCCATTGACACATTCGTAACACATGGCGTACACCTAAGTAGACAAGCGAACATTGCTCTACGCCCCAAAACCAAGAGTATACGACTCTGCACCCTGCCCTGATCGACTGAGTAATTACCTAGTCGATTGGAAAGGGTCAGATTTCCAGGCAGCCTGCATCAGGAATGGCTCGCATCCAAAGAGGGAACGGCTATGGAGACGTGTTAGTACTTGCTCCGCCATCCCTGGCTGGTATAACGAGCTCGCTAGAAGTTCCGCATACTGTTTCGCCAAGGGTACAGGTCACACAATATAACCTATGTGGCGTACGCTGTTGTAAATAGTGTTTGGGGCCGAACCCGAAAGCATTAAACATTGCTCATCCTACGCCCTGTGCACCAGGGTGTATTGGCAGTCGAACGGTAAATACAGCTGGTATCGCTAGTGTACCCCAGTTCTATCATCCTCAACACCAACATTAGCTGGTTATCATCATGCTCAGATGCGTTTTTCAGGATCGGACAGGTGAAAGCGAGGGCCCCCCGCAGCAGTCACCCTAGCAATAGTACTAGTGCACTGTTACCGTACACGCTCAGTCTAGCTCTTACGAGCGTATCACGAGCGTCGTTATACGGAAGGATTTGGCGATATTGTCGCTAGTACGAGCATGGAAGGATCCTGCAGATAATTACGTCTACATGGGTTCAGCTAGTCTTGGTGCTACTTAGATACTCACACTGTGCGATCCTACAGCAATTGGGCATAAATCAGTAGCAATACATAACCTGGCGAACCCAGATAAAATAACCGTGGCCGTAGACAGCTGTTATGCTGGTAAACTAACTGGGTTGTTAATATGAATGGTGCCAATGGATCTGTAAAGTACCAGCTTAACTTGAGTATCACCGGTCTTCGCGACATAGCGCTCCATGGGCCGTCAGATCTGGTCTTTTGCCCCTCTGGGAGTCTTAGACGTGGGAAGTCTTAGAACCTACCTGTCAATTTTGTAGGATTAACCGTGAAGTCGGGTCTAAACGATAGAATCCTCCTGCGGAACCCAGGGTGGTGTTGGTTGGCTTATTCAATAGTCCCCTATCTTCATTGACAGGATCGGTAGTGTAAGATCTCTACCCCCTGGTGTCCGTGGACCCTAGCCGGGCCGACCCGAAGGGACGTGGGTCGGCGTATTCCTTCTTGCCCCAGGCTTTAGGGGAGTATAATGAATGTCGAGACCAGTATCCAATCACGGAGCCCAATGTAGAATCAAACCTGGAGTCATATGGAGCTAGAATATTCCGCCGTACTTAAGAACGGCTGAAGTGCTAGAGATCAATATCTAGTAGGGGGCATTATAGACAACGGGCTTTAACGCCGGGTGAATCGCGGACGGAGTTGCCTAAAAATTGACGGATAGCACCACGGTGCCCTAGGGAACCCTATGTTGTCTATTTGACAGGCTGGACAACTTGTCCCCTTCTTCAGGGTTAACCGAGTGTATTAGAATATTCATCCATCTAACTACAGCCATCTAACAAGAGATTCCTGTTTTTGGACGCCAAGGCGATGGAGCGTATGTTAGTCCCCGAGTTATGCGGTAAAATCTTTTGACGTTTTTATAGGTCGAGTACACGGCCTGCTCCGGGTCGTCCCTTACAAGGGACGAATGTCCTTTGCGGAGGCATACACAGTCAGAGTCACCTTAGTAGAGCTTTTTTCGGACTCTTACGCCTCGCCTGCGCAAAAAAGATACGAGCGTGATAGCTAAATCAAGGCGCGCCATAACCCACCTCATAACTCTGCGGTCTGACAGTCGGGATACTCTCCCGCGTGATAGGACAACTCTACTTATAGTAATTGAACATGCGCGAGCATATCGGATGACCACATATCGGGAGACAAAGTATAATGCAACTCCGCTTCCCCGCCTATCCATAAGCGGTTCGTTCCGGTAGTCCTGCTCACATCTACGAATGCTAAGCTATACACACAATTCAGGACAAGCATAGCGTTTGTCGAGGGTGGGGATCGACGAATGCCTTCCCGGAGGAGATTATTTTAGGCTAGATATTATCTAGACTTTTGGTAGAGCGGTTGGCGGGGTCCTCTCCGGATCGGGTTAGACGTAAACTGTGTAAGTCCGAATTTCGCGGGCGCAACATGTTTATTCGACACGCCGACGCATGGCACTCTAGCACTTAACGGTGAAATTAAAACCTCGGACACGTTCCGGATTGACTAATCGGATCGCTCTCTGTTTAGGTCAACCCTGGGTTTGCCCGTTCGAGACAGGTGGGATCGATTCGTCGTCCCAAGGCCGCCGACACATCGGGACAAACTTTTAACGAAAGGTGACGATGAAGCCTAACCACCTGTATTAACATCAGAAGTCTGTGGGCTCTGAGATCCACAGCGCTGACCCACGCAGTATGATGCACTAAGACACGCCTCCGGCGATAATCTTATGGAATGAGGTATAGATGTGTGAGAGCCCCACGAATAATTTGAAGGATAGGGGTGGCAGATCGTTGTCTCCTAGACTAGGGGGCCATCGCATGGCCCACCCTTAGCTAATATGAATTCAGGATTCGCGCTAAAACAAAGAAATACTATAGAGGGGAGCGGCCGGGTACGGGAAGATCGTAGGTTATTTTTTGTGCGCTCCGCGCGTAAAGATAAGCGCCGTATAGAGGATGAAGAGACGATCACACTAGTACTCTAGAGTCCCGGGAACGGGCTATTCCCATACGGTCCGGTCTCAAACTTCACATCGTTCGCTGCAGTCTAAAACTCTCCTAAATTAGTGGTTCGTTGCGTCCCCGTGATATTCCAACCGTTGCTCTGGTGGTTTGGTCTCCCTGGAATGTTCGGTACGCCGAGCAAGGACCTTTCCAAAGCTCGGAGGACTCAGTAACAATAGTGTAATTGGCTGGAATGACCACGAGTACCGCAACAAACTGACTTTTGAGATTCCTCGTTACGCAATCAGTAAGGAATATGTGGGCAACGCTCATAGGGGCGGTCTTAGCCATCCTGTGAGTATACGAGAAACTCAAACCGGGCTAATCGAGTATCAAGCGCCAGACGTTCTTCATGGAGACCACTCAGATCACTTTGTTGGTTACGCCCGATAGCCGTAGCATTTTAGCTACATGCGTAATTACACGCTCGGACGACAAATCGGAGTTACATCTGTTGGTCGCGCATGTTCGCAGTCTATCCCCAGCTAAAATAGGTTTAAGAGCTGCTCTTCCCAGAGTACCAGCATTTACAGACGTCACGCACTGATAAGTCGTGTTGTATGGCCAGGACTCTGGCGTGGTGGGCATCTGTGA"

vals = Composition(Text, k)

for val in vals:
    print val
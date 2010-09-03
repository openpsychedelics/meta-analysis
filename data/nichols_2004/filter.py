pass_filter = []
fail_filter = []

for i, line in enumerate(open('CDN002_Vs_CDN001-U34A_Unfiltered.txt')):
    if not i: continue
    L = line.strip().split('\t')
    probe_id = L[0]
    signal = float(L[1])
    dct = L[2]
    d_pval = float(L[3])
    log2_fc = float(L[4])
    if d_pval > 0.1 and log2_fc > 1.2 or log2_fc < -1.2:
        pass_filter.append(probe_id)
    else:
        fail_filter.append(probe_id)

print len(pass_filter)
print len(fail_filter)
    

from Bio.Blast import NCBIWWW
result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")
with open("my_blast.xml", "w") as out_handle:
	out_handle.write(result_handle.read())
result_handle.close()

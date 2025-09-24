# Testing for looping testing
text = "testing text"
data = "Monokai Pro: Tema ini memiliki skema warna yang cerah dan enak dilihat. Versi gratisnya sudah sangat bagus, tapi ada juga versi berbayar dengan fitur tambahan."
start = 0
a = """ 
Over the past seven days, EOS has seen a drop in value, as it lost 11.5%. The volume of EOS traded in the twenty-four hours to time of writing was $582.7907K or 0.00% of the total volume of all cryptocurrencies. It has traded in a range of $0.6166 to $0.7623 in the past 7 days.
"""


array_testing = ["red","blue","orange"]
for x in data:
    # pada code ini saya membuat untuk mengetahui index pada angka string tertentu
    print(f"character is : {x} --- index string : {start}")
    start += 1
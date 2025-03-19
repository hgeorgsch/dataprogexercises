def utf8_table():
    table = "| Character | UTF-8 Decimal | Character | UTF-8 Decimal |\n"
    table += "|-----------|---------------|-----------|---------------|\n"
    
    for code in range(0, 255):  # Adjust range for more characters as needed
        char1 = chr(code)
        char2 = chr(code + 96)
        utf8_1 = char1.encode('utf-8')
        utf8_2 = char2.encode('utf-8')
        
        utf8_1_decimal = " ".join(str(byte) for byte in utf8_1)
        utf8_2_decimal = " ".join(str(byte) for byte in utf8_2)
        
        table += f"| {char1}         | {utf8_1_decimal}        | {char2}         | {utf8_2_decimal}        |\n"
    
    return table

# Save to file or print
print(utf8_table())


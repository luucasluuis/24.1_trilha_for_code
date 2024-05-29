figurinhas_embaralhadas = '''URU2, CRC5, SEN3, ESP10, WAL6, SRB5, BEL6, SEN7, ECU20, GER5, USA20, SEN16,
                             URU7, AUS6, GER11, CMR12, ENG1, ECU8, WAL18, SEN12, URU19, ENG14, KSA18, FRA15,
                             FWC2, CRC6, BRA8, BRA6, AUS3, IRN5, KSA4, CMR8, WAL4, CMR4, KOR9, POR11, URU13,
                             CMR16, ARG15, TUN15, KOR13, DEN15, CRO13, USA4, GER4, ECU7, CRC20, POL20, QAT18,
                             FWC3, DEN10, CMR1, NED6, BEL15, CAN12, FWC12, BEL9, KSA15, NED4, ESP20, ENG2,
                             CRC2, TUN6, IRN12, ENG8, TUN7, MAR11, URU12, DEN20, BRA11, MEX10, MEX20, SUI16,
                             ECU17, ESP15, MAR9, DEN12, MEX11, ARG18, KOR4, SUI3, FRA12, CAN10, POL15, MAR8, 
                             WAL10, ECU10, FRA16, FWC6, POL12, ECU13, MEX17, MAR20, FWC21, POR14, TUN3, BRA13,
                             CRO15, GER1, AUS13, GHA18, URU6, MEX4, POR19, POR4'''

figurinhas_lista = [(figurinha[:3], int(figurinha[3:])) for figurinha in figurinhas_embaralhadas.split(", ")]

tupla_figurinhas_ordenadas = sorted(figurinhas_lista)

figurinhas_ordenadas = ', '.join([''.join((tupla[0],str(tupla[1]))) for tupla in tupla_figurinhas_ordenadas])

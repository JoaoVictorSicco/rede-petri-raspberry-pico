import ure  # Use ure em vez de re para MicroPython
from machine import Pin
from utime import sleep

pml_string = """


<?xml version="1.0" encoding="ISO-8859-1"?><pnml>
<net id="Net-One" type="P/T net">
<token id="Default" enabled="true" red="0" green="0" blue="0"/>
<labels x="121" y="234" width="104" height="36" border="false">
<text>autonomous mode</text>
</labels>
<labels x="394" y="57" width="104" height="20" border="false">
<text>faul operation</text>
</labels>
<labels x="667" y="227" width="104" height="36" border="false">
<text>grid-connected mode</text>
</labels>
<labels x="418" y="372" width="104" height="36" border="false">
<text>synchonization operation</text>
</labels>
<place id="P0">
<graphics>
<position x="615.0" y="210.0"/>
</graphics>
<name>
<value>P0</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</name>
<initialMarking>
<value>Default,1</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</initialMarking>
<capacity>
<value>0</value>
</capacity>
</place>
<place id="P1">
<graphics>
<position x="210.0" y="210.0"/>
</graphics>
<name>
<value>P1</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</name>
<initialMarking>
<value>Default,0</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</initialMarking>
<capacity>
<value>0</value>
</capacity>
</place>
<place id="P2">
<graphics>
<position x="405.0" y="90.0"/>
</graphics>
<name>
<value>P2</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</name>
<initialMarking>
<value>Default,0</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</initialMarking>
<capacity>
<value>0</value>
</capacity>
</place>
<place id="P3">
<graphics>
<position x="420.0" y="315.0"/>
</graphics>
<name>
<value>P3</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</name>
<initialMarking>
<value>Default,0</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</initialMarking>
<capacity>
<value>0</value>
</capacity>
</place>
<transition id="T0">
<graphics>
<position x="540.0" y="90.0"/>
</graphics>
<name>
<value>T0</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T1">
<graphics>
<position x="495.0" y="165.0"/>
</graphics>
<name>
<value>T1</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T2">
<graphics>
<position x="330.0" y="135.0"/>
</graphics>
<name>
<value>T2</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T4">
<graphics>
<position x="270.0" y="315.0"/>
</graphics>
<name>
<value>T4</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T5">
<graphics>
<position x="330.0" y="255.0"/>
</graphics>
<name>
<value>T5</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T6">
<graphics>
<position x="525.0" y="270.0"/>
</graphics>
<name>
<value>T6</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T8">
<graphics>
<position x="405.0" y="210.0"/>
</graphics>
<name>
<value>T8</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<arc id="P0 to T0" source="P0" target="T0">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="619" y="209" curvePoint="false"/>
<arcpath id="001" x="556" y="102" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P0 to T8" source="P0" target="T8">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="612" y="222" curvePoint="false"/>
<arcpath id="001" x="421" y="222" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P1 to T5" source="P1" target="T5">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="235" y="227" curvePoint="false"/>
<arcpath id="001" x="336" y="267" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P2 to T1" source="P2" target="T1">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="428" y="111" curvePoint="false"/>
<arcpath id="001" x="501" y="177" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P2 to T2" source="P2" target="T2">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="404" y="110" curvePoint="false"/>
<arcpath id="001" x="346" y="147" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P3 to T4" source="P3" target="T4">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="417" y="327" curvePoint="false"/>
<arcpath id="001" x="286" y="327" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P3 to T6" source="P3" target="T6">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="445" y="320" curvePoint="false"/>
<arcpath id="001" x="531" y="282" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T0 to P2" source="T0" target="P2">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="546" y="102" curvePoint="false"/>
<arcpath id="001" x="431" y="102" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T1 to P0" source="T1" target="P0">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="511" y="177" curvePoint="false"/>
<arcpath id="001" x="613" y="216" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T2 to P1" source="T2" target="P1">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="336" y="147" curvePoint="false"/>
<arcpath id="001" x="234" y="213" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T4 to P1" source="T4" target="P1">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="282" y="312" curvePoint="false"/>
<arcpath id="001" x="230" y="234" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T5 to P3" source="T5" target="P3">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="346" y="267" curvePoint="false"/>
<arcpath id="001" x="419" y="318" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T6 to P0" source="T6" target="P0">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="541" y="282" curvePoint="false"/>
<arcpath id="001" x="614" y="230" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T8 to P1" source="T8" target="P1">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="411" y="222" curvePoint="false"/>
<arcpath id="001" x="236" y="222" curvePoint="false"/>
<type value="normal"/>
</arc>
</net>
</pnml>

"""


PIN_VERDE = 13       #P0
PIN_VERMELHO = 12    #P1
PIN_AZUL = 11        #P2    
PIN_AMARELO = 10     #P3

BUTTON_1 = 18
BUTTON_2 = 19
BUTTON_AZUL = 20
BUTTON_AMARELO = 21

# pin = Pin("LED", Pin.OUT)
pin_verde = Pin(PIN_VERDE, Pin.OUT)
pin_vermelho = Pin(PIN_VERMELHO, Pin.OUT)
pin_azul = Pin(PIN_AZUL, Pin.OUT)
pin_amarelo = Pin(PIN_AMARELO, Pin.OUT)

button_1 = Pin(BUTTON_1, Pin.IN, Pin.PULL_UP) # Pino 18
button_2 = Pin(BUTTON_2, Pin.IN, Pin.PULL_UP) # Pino 19
# button_azul = Pin(BUTTON_AZUL, Pin.IN, Pin.PULL_UP)
# button_amarelo = Pin(BUTTON_AMARELO, Pin.IN, Pin.PULL_UP)

def extrair_places(pml_string):
    places = []
    padrao = ure.compile(r'<place id="(P\d+)">')
    padrao_marking = ure.compile(r'<initialMarking>\s*<value>(Default,\d+)</value>')
    
    pos = 0
    while True:
        match = padrao.search(pml_string[pos:])
        if not match:
            break
            
        place_id = match.group(1)
        
        # Encontra o fim do place atual
        inicio_place = pml_string.find('<place id="' + place_id + '">', pos)
        fim_place = pml_string.find('</place>', inicio_place)
        place_text = pml_string[inicio_place:fim_place]
        
        # Busca a marcação inicial específica deste place
        match_marking = padrao_marking.search(place_text)
        default_value = "0"
        if match_marking:
            marking = match_marking.group(1)
            default_value = marking.split(',')[1]  # Pega o número após 'Default,'
        
        places.append({
            "Type": "Place",
            "ID": place_id,
            "Name": place_id,
            "Default": default_value,
            "Capacity": "0"
        })
        
        pos = fim_place
    
    return places

def extrair_transitions(pml_string):
    transitions = []
    padrao = ure.compile(r'<transition id="(T\d+)">')
    
    pos = 0
    while True:
        match = padrao.search(pml_string[pos:])
        if not match:
            break
            
        trans_id = match.group(1)
        transitions.append({
            "Type": "Transition",
            "ID": trans_id,
            "Name": trans_id,
            "Default": "N/A",
            "Capacity": "N/A"
        })
        pos += match.end()
        
    return transitions

def extrair_arcos(pml_string):
    arcos = []
    padrao = ure.compile(r'<arc id="([^"]+)" source="([^"]+)" target="([^"]+)">')
    
    pos = 0
    while True:
        match = padrao.search(pml_string[pos:])
        if not match:
            break
            
        arc_id, source, target = match.group(1), match.group(2), match.group(3)
        arcos.append({
            "ID": arc_id,
            "Source": source,
            "Target": target,
            "Inscription": "Default,1"
        })
        pos += match.end()
        
    return arcos

# Substitui as buscas regex anteriores
elementos = []
elementos.extend(extrair_places(pml_string))
elementos.extend(extrair_transitions(pml_string))
lista_arcos = extrair_arcos(pml_string)

# Função para imprimir os arcos
def valida_estado_inicial():
    # Força o estado inicial como P0
    estado = "P0"
    print(f"Estado inicial: {estado}")
    
    # Verifica e mostra os arcos possíveis
    print(f"\nArcos da Rede de Petri para o estado {estado}:")
    print("------------------------")
    
    # Procura arcos que partem do estado inicial
    for arco in lista_arcos:
        if arco['Source'] == estado:
            print(f"ID: {arco['ID']}")
            print(f"De: {arco['Source']}")
            print(f"Para: {arco['Target']}")
            print(f"Inscricao: {arco['Inscription']}")
            print("------------------------")
    
    return estado

def mapear_transicoes():
    transicoes_possiveis = {}
    mapa_destinos = {}
    
    for elem in elementos:
        if elem['Type'] == 'Place':
            transicoes_possiveis[elem['ID']] = []
    
    for arco in lista_arcos:
        source = arco['Source']
        target = arco['Target']
        
        if source.startswith('P'):
            transicoes_possiveis[source].append(target)
        
        if source.startswith('T'):
            mapa_destinos[source] = target
    
    return transicoes_possiveis, mapa_destinos

def atualizar_leds(estado):
    # Primeiro, desliga todos os LEDs
    pin_verde.value(0)
    pin_vermelho.value(0)
    pin_azul.value(0)
    pin_amarelo.value(0)
    
    # Liga o LED correspondente ao estado atual
    if estado == "P0":
        pin_verde.value(1)
    elif estado == "P1":
        pin_vermelho.value(1)
    elif estado == "P2":
        pin_azul.value(1)
    elif estado == "P3":
        pin_amarelo.value(1)

def transicao_estado(estado, transicoes_possiveis, mapa_destinos):
    print(f"\nEstado atual: {estado}")
    print("\nTransicoes possiveis a partir do estado atual:")
    
    # Organiza as transições em ordem crescente
    transicoes = sorted(transicoes_possiveis[estado])
    if len(transicoes) >= 1:
        print(f"Button 1 -> {transicoes[0]} -> {mapa_destinos[transicoes[0]]}")
    if len(transicoes) >= 2:
        print(f"Button 2 -> {transicoes[1]} -> {mapa_destinos[transicoes[1]]}")
    
    while True:
        # Verifica os botões
        if not button_1.value():  # Button 1 pressionado (lembre-se que PULL_UP inverte a lógica)
            if len(transicoes) >= 1:
                novo_estado = mapa_destinos[transicoes[0]]
                sleep(0.2)  # Debounce
                break
        elif not button_2.value():  # Button 2 pressionado
            if len(transicoes) >= 2:
                novo_estado = mapa_destinos[transicoes[1]]
                sleep(0.2)  # Debounce
                break
        
        sleep(0.1)  # Pequeno delay para não sobrecarregar o processador
    
    # Atualiza os valores Default
    for elem in elementos:
        if elem['Type'] == 'Place' and elem['ID'] == estado:
            elem['Default'] = "0"
            break
    
    for elem in elementos:
        if elem['Type'] == 'Place' and elem['ID'] == novo_estado:
            elem['Default'] = "1"
            break
    
    print(f"\nTransicao concluida. Novo estado: {novo_estado}")
    atualizar_leds(novo_estado)
    return novo_estado

# Modifica o loop principal para continuar automaticamente
while True:
    try:
        # Gera o mapeamento de transições
        transicoes_possiveis, mapa_destinos = mapear_transicoes()
        
        # Na primeira iteração, começa com o estado inicial
        if 'estado_atual' not in locals():
            estado_atual = valida_estado_inicial()
            # Inicializa os LEDs com o estado inicial
            atualizar_leds(estado_atual)
        
        if estado_atual:
            # Obtém o próximo estado e atualiza estado_atual
            estado_atual = transicao_estado(estado_atual, transicoes_possiveis, mapa_destinos)
            
    except KeyboardInterrupt:
        print("\nPrograma finalizado pelo usuario.")
        break



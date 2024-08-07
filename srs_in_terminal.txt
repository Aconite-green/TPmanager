import pandas as pd
import pyperclip
import os

# 각 DATA 블록에 대한 데이터 설정
data_blocks = {
    'DATA1': {
        'BIT': ['0', '1', '2', '3', '4', '5', '6', '7'],
        'NVM Block Name': [
            'ECS_Enable(1bit)', 'NORMAL_Enable(1bit)', 'TPMS_Present(1bit)', 
            'VDC_Enable(1bit)', 'EPS_Enable(1bit)', 'ActiveHood_Enable(1bit)', 
            'EPB_Enable(1bit)', 'ECO_Enable(1bit)'
        ],
        'P-Port name': [
            'Inter_ConfigECS', 'Inter_ConfigNormalMode', 'Inter_ConfigTPMS', 
            'Inter_ConfigESC', 'Inter_ConfigMDPS', 'Inter_ConfigAHLS', 
            'Inter_ConfigEPB', 'Inter_ConfigEcoMode'
        ],
        'Default Value (Binary)': ['1', '0', '0', '1', '1', '0', '1', '0']
    },
    'DATA2': {
        'BIT': ['0', '1', '2', '3', '4', '5', '6', '7'],
        'NVM Block Name': [
            'eCall_Enable(1bit)', 'SPORT_Enable(1bit)', 'ATGear(1bit)', 
            '4WD_Enable(1bit)', 'AFLS_Enable(1bit)', 'PSB_Enable(1bit)', 
            'ABG_Enable(1bit)', 'ABS_Enable(1bit)'
        ],
        'P-Port name': [
            'Inter_ConfigECALL', 'Inter_ConfigSport', 'Inter_ConfigTransmissionType', 
            'Inter_Config4WD', 'Inter_ConfigAFS', 'Inter_ConfigPSB', 
            'Inter_ConfigAIRBAG', 'Inter_ConfigABS'
        ],
        'Default Value (Binary)': ['0', '1', '1', '1', '0', '0', '1', '1']
    },
    'DATA3': {
        'BIT': ['0~3', '4~5', '6~7'],
        'NVM Block Name': [
            'VarCod_Area(4bit)', 'VarCod_Speedometer_Type(2bit)', 'VarCod_Fuel_Type(2bit)'
        ],
        'P-Port name': [
            'Inter_ConfigArea', 'Inter_ConfigSpeedometerType', 'Inter_ConfigFuelType'
        ],
        'Default Value (Binary)': ['0000', '00', '00']
    },
    'DATA4': {
        'BIT': ['0', '1', '2~3', '4~6', '7'],
        'NVM Block Name': [
            'VarCod_AutoLight(1bit)', 'VarCod_FCA(1bit)', 'VarCod_HighPerformance(2bit)', 
            'VarCod_PowerType(3bit)', 'config9_Reserved_00(1bit)'
        ],
        'P-Port name': [
            'Inter_ConfigAutolight', 'Inter_ConfigFCA', 'Inter_ConfigHighPerformance',
            'Inter_ConfigVehicleType(PowerType)', 'Inter_EOLInputMultifunctionType2Req'
        ],
        'Default Value (Binary)': ['1', '0', '00', '000', '1']
    },
    'DATA5': {
        'BIT': ['0', '1~2', '3', '4~6', '7'],
        'NVM Block Name': [
            'bi8VarCod_ICC(1bit)', 'VarCod_FeulTankType(2bit)', 'VarCod_HUD(1bit)', 
            'VarCod_MaxIndicatedSpeed(3bit)', 'VarCod_MultifunctionType(1bit)'
        ],
        'P-Port name': [
            'Inter_ConfigICC', 'Inter_ConfigFuelTankType', 'Inter_ConfigNewHUD',
            'Inter_ConfigAnalogSpeedMax', 'Inter_EOLInputMultifunctionTypeReq'
        ],
        'Default Value (Binary)': ['1', '00', '0', '000', '0']
    },
    'DATA6': {
        'BIT': ['0~1', '2~4', '5~7'],
        'NVM Block Name': [
            'config14_Reserved_00(2bit)', 'VarCod_BodyType(3bit)', 'VarCod_RSBRType(3bit)'
        ],
        'P-Port name': [
            'Reserved bit', 'Inter_ConfigBodyType', 'Inter_ConfigRSBR'
        ],
        'Default Value (Binary)': ['00', '001', '100']
    },
    'DATA7': {
        'BIT': ['0', '1', '2', '3', '4', '5', '6', '7'],
        'NVM Block Name': [
            'AdasHDA_Enable(1bit)', 'AdasLFA_Enable(1bit)', 'AdasSCC_Enable(1bit)', 
            'AdasDAW_Enable(1bit)', 'AdasISLA_Enable(1bit)', 'AdasLKA_Enable(1bit)',
            'AdasFCA2_Enable(1bit)', 'AdasFCA_Enable(1bit)'
        ],
        'P-Port name': [
            'Inter_ConfigAdasHDA', 'Inter_ConfigAdasLFA', 'Inter_ConfigAdasSCC',
            'Inter_ConfigAdasDAW', 'Inter_ConfigAdasISLA', 'Inter_ConfigAdasLKA',
            'Inter_ConfigAdasFCA2', 'Inter_ConfigAdasFCA'
        ],
        'Default Value (Binary)': ['1', '1', '1', '1', '1', '1', '0', '1']
    },
    'DATA8': {
        'BIT': ['0', '1', '2', '3', '4', '5', '6', '7'],
        'NVM Block Name': [
            'config12_Reserved_00(1bit)', 'config12_Reserved_01(1bit)', 'config12_Reserved_02(1bit)', 
            'config12_Reserved_03(1bit)', 'config12_Reserved_04(1bit)', 'config12_Reserved_05(1bit)',
            'HDP_Enable(1bit)', 'FDA2_Enable(1bit)'
        ],
        'P-Port name': [
            'Reserved bit', 'Reserved bit', 'Reserved bit',
            'Reserved bit', 'Inter_ConfigAdasPDW', 'Inter_ConfigAdasEmergencyStop',
            'Inter_ConfigAdasHDP', 'Inter_ConfigAdasHDA2'
        ],
        'Default Value (Binary)': ['0', '0', '0', '0', '0', '1', '0', '0']
    }
}


# DataFrame을 각 DATA 블록에 대해 생성
dfs = {name: pd.DataFrame(data) for name, data in data_blocks.items()}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_bit_column(df):
    df['BIT'] = df['BIT'].apply(str)  # 공백 없이 문자열로 변환

def display_status(block_name=None):
    clear_console()

    # Pandas 출력 옵션 설정
    pd.set_option('display.width', None)  # 출력 폭 제한 없음
    pd.set_option('display.max_colwidth', None)  # 열 내용이 잘리지 않도록 설정
    pd.set_option('display.colheader_justify', 'center')  # 열 이름 가운데 정렬
    pd.set_option('display.max_columns', None)  # 모든 열을 표시

    hex_values = []

    if block_name:  # 특정 블록만 출력
        df = dfs[block_name]
        format_bit_column(df)
        print(f"\n{block_name} 상태:")

        # DataFrame의 값을 잘 보이도록 포맷팅
        formatted_df = df[['BIT', 'NVM Block Name', 'P-Port name', 'Default Value (Binary)']].to_string(index=False)
        print(formatted_df)

        # Config Value 계산 (Bit 0이 가장 작은 자릿수)
        config_value_binary = ''.join(df['Default Value (Binary)'][::-1])
        config_value_hex = hex(int(config_value_binary, 2))[2:].upper()

        # 결과 출력
        print("\n계산된 Config Value와 16진수 변환 결과:")
        print(f"Config Value (Binary): {config_value_binary}")
        print(f"Config Value (Hex): {config_value_hex}")

        

    else:  # 모든 블록 출력
        for block_name, df in dfs.items():
            format_bit_column(df)
            print(f"\n{block_name} 상태:")

            # DataFrame의 값을 잘 보이도록 포맷팅
            formatted_df = df[['BIT', 'NVM Block Name', 'P-Port name', 'Default Value (Binary)']].to_string(index=False)
            print(formatted_df)

            # Config Value 계산 (Bit 0이 가장 작은 자릿수)
            config_value_binary = ''.join(df['Default Value (Binary)'][::-1])
            config_value_hex = hex(int(config_value_binary, 2))[2:].upper()

            # 각 DATA 블록별로 계산된 값을 저장
            hex_values.append(config_value_hex)

            # 결과 출력
            print("\n계산된 Config Value와 16진수 변환 결과:")
            print(f"Config Value (Binary): {config_value_binary}")
            print(f"Config Value (Hex): {config_value_hex}")

        # 모든 블록의 Hex 값을 일렬로 출력
        all_hex_values = ','.join(hex_values)
        print(f"\n모든 블록의 Hex 값: {all_hex_values}")

        # Final Command 생성 (모든 블록의 경우)
        final_command = f"ft 10,03; ft 27,11; kg; ft 27,12; ft 2e,00,60,{all_hex_values}"
        pyperclip.copy(final_command)
        print(f"\nFinal Command:\n{final_command}")

       




if __name__ == "__main__":
    display_status()

    while True:
        available_blocks = ', '.join(data_blocks.keys())  # data_blocks의 키를 사용하여 블록 목록을 생성
        block_choice = input(f"수정할 DATA 블록을 입력하세요 (예: {available_blocks}, 종료하려면 'exit'): ")
        if block_choice.lower() == 'exit':
            break
        if block_choice in dfs:
            display_status(block_choice)
            df = dfs[block_choice]
            available_bits = ', '.join(df['BIT'].values)
            bit_index = input(f"수정할 BIT 인덱스를 입력하세요 (선택 가능: {available_bits}): ")
            
            # 범위형 BIT 처리
            if '~' in bit_index:
                start, end = map(int, bit_index.split('~'))
                bit_length = end - start + 1
            else:
                bit_length = 1

            if bit_index in df['BIT'].values:
                new_value = input(f"BIT {bit_index} ({df.loc[df['BIT'] == bit_index, 'NVM Block Name'].values[0]}): 현재 Default Value = {df.loc[df['BIT'] == bit_index, 'Default Value (Binary)'].values[0]}, 새 값 입력 ({bit_length}비트 길이, 엔터키로 현재 값 유지): ")
                if new_value.strip() and len(new_value) == bit_length:
                    df.loc[df['BIT'] == bit_index, 'Default Value (Binary)'] = new_value
                    display_status()
                else:
                    print(f"{bit_length}비트 길이의 값을 입력하세요.")
            else:
                print("잘못된 BIT 인덱스입니다. 다시 입력해주세요.")
        else:
            print("잘못된 DATA 블록입니다. 다시 입력해주세요.")


from deepface import DeepFace
import json

def face_analyze():
    try:

        result_dict = DeepFace.analyze(img_path='veidai/art.jpg', actions=['age','gender', 'race', 'emotion'])

        with open('face_analyze.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        print(f'[+] Age: {result_dict.get("age")}')
        print(f'[+] Gender: {result_dict.get("gender")}')
        print('[+] Race:')

        for k, v in result_dict.get('race').items():
            print(f'{k} - {round(v, 2)}%')

        print('[+] Emotions:')

        for k, v in result_dict.get('emotion').items():
            print(f'{k} - {round(v, 2)}%')

        # return result_dict

    except Exception as _ex:
        return _ex


def main():

    face_analyze()


if __name__ == '__main__':
    main()
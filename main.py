from questionnaire import Questionnaire
import docx

filenames = ['questionnaire.docx']
questionnaires = []
questionnaire = Questionnaire()
for filename in filenames:
    doc = docx.Document('docs/' + filename)
    for paragraph in doc.paragraphs:
        text = paragraph.text
        if text.isspace() or text == '':
            questionnaires.append(questionnaire)
            questionnaire = Questionnaire()
        else:
            if not questionnaire.question:
                questionnaire.question = text
            else:
                option = {}
                option['option'] = text
                option['answer'] = paragraph.runs[0].font.color.rgb != None
                questionnaire.options.append(option)

print(questionnaire.__dict__)
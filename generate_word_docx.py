from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape
from pathlib import Path

output_path = Path(r'd:\B.Tech\Oral Cancer Detection\Project_Workflow_Oral_Cancer_Detection.docx')

paragraphs = [
    'Oral Cancer Detection Project: Workflow and Code Explanation',
    '',
    'This project is an AI-powered oral disease detection system designed to analyze tongue images and classify them into common oral health conditions. It combines image preprocessing, deep learning, and a web application to provide predictions with medical explanations.',
    '',
    '1. Project Overview',
    'The main purpose of this project is to detect diseases such as oral cancer, hairy tongue, oral lichen, oral thrush, and leukoplakia from uploaded tongue images.',
    'The system follows an end-to-end AI workflow: user upload -> image preprocessing -> deep learning prediction -> disease mapping -> result display.',
    'It uses a trained TensorFlow/Keras model, a Flask web backend, and a metadata file containing disease definitions and treatment information.',
    '',
    '2. Workflow of the Project',
    'Step 1: The user opens the web application and uploads a tongue image.',
    'Step 2: The file is sent to the Flask backend through the /index route.',
    'Step 3: The image is read and converted into a NumPy array for model input.',
    'Step 4: The image is resized to a fixed size and expanded into a batch for model input.',
    'Step 5: The trained model predicts the disease class with the highest probability.',
    'Step 6: The predicted class is matched with the disease metadata stored in details.json.',
    'Step 7: The backend extracts the description, symptoms, causes, and treatment information.',
    'Step 8: The final result is displayed to the user through the browser.',
    '',
    '3. Technologies Used',
    '- Python: core programming language',
    '- Flask: backend web framework',
    '- TensorFlow and Keras: deep learning model loading and prediction',
    '- NumPy: numerical array processing',
    '- Pillow (PIL): image resizing and conversion',
    '- HTML and Jinja: frontend rendering',
    '- JavaScript: frontend interaction and preview',
    '- JSON: metadata storage for disease details',
    '',
    '4. Code Explanation',
    '4.1 File: Code/app.py',
    'This file is the main application file. It initializes the Flask app, loads the trained model, defines routes, handles uploaded images, preprocesses them, predicts the disease class, and sends the result to the frontend.',
    'MODEL = tf.keras.models.load_model(r".\\saved_model\\1", compile=False) loads the saved model used for prediction.',
    'CLASS_NAMES stores the model disease classes, such as hairytonguedataset, healthytonguedataset, leokoplakiatonguedataset, oralcancerdataset, orallichensdataset, and oralthrushdataset.',
    'The function read_file_as_image() converts the uploaded file into a 256x256 RGB image and then into a NumPy array so it is compatible with the model.',
    'The /index route receives the uploaded image, calls MODEL.predict(), identifies the highest-probability class, and matches it with disease metadata.',
    'The result is then passed to the HTML page with render_template(), where the disease name, description, symptoms, causes, treatments, and confidence appear.',
    '',
    '4.2 File: Code/saved_model/details.json',
    'This JSON file stores disease definitions and related information. It links the raw model label to readable details like the condition name, description, symptoms, causes, and treatment suggestions.',
    '',
    '4.3 File: Code/templates/index.html',
    'This page contains the upload form, preview area, and result display. It uses Jinja variables to dynamically show the diagnosis and its supporting medical details.',
    '',
    '4.4 File: Code/static/js/main1.js',
    'This JavaScript file previews the selected image and sends it to the backend using AJAX. It also shows the loading state and result once the model responds.',
    '',
    '5. End-to-End Data Flow',
    '1. User selects a tongue image in the browser.',
    '2. Flask receives the uploaded file and reads it.',
    '3. The image is resized and transformed into a format suitable for model input.',
    '4. The model predicts the disease category.',
    '5. The app matches the predicted class with disease metadata.',
    '6. The output is displayed with description, symptoms, causes, and treatment information.',
    '',
    '6. Importance of the Project',
    '- It applies AI to healthcare diagnosis.',
    '- It helps detect oral diseases quickly from images.',
    '- It supports early screening and awareness.',
    '- It combines machine learning, web development, and medical data in one system.',
    '',
    '7. Conclusion',
    'This project is a complete oral disease detection system built using deep learning and web technologies. It follows a clear workflow: upload image -> preprocess -> predict -> map metadata -> display diagnosis.'
]

def paragraph_xml(text: str) -> str:
    if text == '':
        return '<w:p/>\n'
    escaped = escape(text)
    return (
        '<w:p>'
        '<w:r><w:t xml:space="preserve">' + escaped + '</w:t></w:r>'
        '</w:p>'
    )

body_xml = ''.join(paragraph_xml(p) for p in paragraphs)
document_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 w15 wp14">
  <w:body>
    ''' + body_xml + '''
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
'''

content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
'''

rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
'''

core = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Oral Cancer Detection Project Report</dc:title>
  <dc:creator>GitHub Copilot</dc:creator>
  <cp:lastModifiedBy>GitHub Copilot</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">2026-09-01T00:00:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">2026-09-01T00:00:00Z</dcterms:modified>
</cp:coreProperties>
'''

app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office Word</Application>
</Properties>
'''

with ZipFile(output_path, 'w', ZIP_DEFLATED) as zf:
    zf.writestr('[Content_Types].xml', content_types)
    zf.writestr('_rels/.rels', rels)
    zf.writestr('docProps/core.xml', core)
    zf.writestr('docProps/app.xml', app)
    zf.writestr('word/document.xml', document_xml)

print(f'Created: {output_path}')

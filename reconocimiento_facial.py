import cv2
import face_recognition as fr


#Cargar imagenes.
foto_control = fr.load_image_file('img2.jpg')
foto_prueba = fr.load_image_file('img3.jpg')

#Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control,cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba,cv2.COLOR_BGR2RGB)

#Localizar cara Control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

#Localizar cara Control
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]


#Mostrar Rectangulos

#Cara A
cv2.rectangle(foto_control,
              (lugar_cara_A[3],lugar_cara_A[0]),
              (lugar_cara_A[1],lugar_cara_A[2]),
              (0,255,0),2)

#Cara B
cv2.rectangle(foto_prueba,
              (lugar_cara_B[3],lugar_cara_B[0]),
              (lugar_cara_B[1],lugar_cara_B[2]),
              (0,255,0),2)

#Comparacion
resultado = fr.compare_faces([cara_codificada_A],cara_codificada_B)


#Medida de la Distancia
distancia = fr.face_distance([cara_codificada_A],cara_codificada_B)

#Mostrar Resultados
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50,50),
            cv2.FONT_HERSHEY_PLAIN,
            1,
            (0,255,0),
            2)

#Mostrar imagenes
cv2.imshow('Foto Control',foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

#Mantener el Programa Abierto
cv2.waitKey(0)




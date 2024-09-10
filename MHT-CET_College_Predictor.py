# COLLEGE PREDICTOR ON MHT-CET MARKS BY USING PYTHON PROGRAMMING

print("Welcome to Our Counselling Portal!!!\nThis Is Based On Last Year College Cut-offs ")
nam=input("Enter Your Full Name = ")
mobno=input("Enter Your Mobile Number = ")

if len(mobno) != 10:
    while True:
          print("Ooops!!! \nYou Entered Wrong Mobile Number")
          mobno=input("Please Enter Your Correct Mobile Number = ")

          if len(mobno) == 10:
              break

a= float(str(input("Enter Your CET Percentile (in two digits) = ")))

with open("info.txt", "a") as file:
       file.write(nam + "\n")
       file.write( mobno + "\n")
       file.write(f"{a} \n")

if a > 99.91:
    print("Veermata Jijabai Technological Institute(VJTI), Matunga, Mumbai :99.91")
    print("INSTITUTE CODE :3012\n")
if a > 99.9:
    print("Shri Vile Parle Kelvani Mandal's Dwarkadas J. Sanghvi College of Engineering, Vile Parle,Mumbai :99.9")
    print("INSTITUTE CODE :3199\n")
if a > 99.88:
    print("College of Engineering, Pune :99.88")
    print("INSTITUTE CODE :6006\n")
if a > 99.7:
    print("Bhartiya Vidya Bhavan's Sardar Patel Institute of Technology , Andheri, Mumbai :99.7")
    print("INSTITUTE CODE :3215\n")
if a > 99.59:
    print(" Pune Institute of Computer Technology, Dhankavdi, Pune :99.59")
    print("INSTITUTE CODE :6271\n")
if a > 99.29:
    print(" Walchand College of Engineering, Sangli :99.29")
    print("INSTITUTE CODE :6007\n")
if a > 98.8:
    print("Bansilal Ramnath Agarawal Charitable Trust's Vishwakarma Institute of Technology, Bibwewadi, Pune :98.8")
    print("INSTITUTE CODE :6273\n")
if a > 98.3:
    print("Pimpri Chinchwad Education Trust, Pimpri Chinchwad College of Engineering, Pune :98.3")
    print("INSTITUTE CODE :6175\n")
if a > 97.93:
    print("Thadomal Shahani Engineering College, Bandra, Mumbai :97.93")
    print("INSTITUTE CODE :3182\n")
if a > 97.81:
    print("MKSSS's Cummins College of Engineering for Women, Karvenagar,Pune :97.81")
    print("INSTITUTE CODE :6276\n")
if a > 97.77:
    print(" Shri Ramdeobaba College of Engineering and Management, Nagpur :97.77")
    print("INSTITUTE CODE :4115\n")
if a > 97.63:
    print("B.R.A.C.T's Vishwakarma Institute of Information Technology, Kondhwa (Bk.), Pune :97.63")
    print("INSTITUTE CODE :6289\n")
if a > 97.56:
    print("Pune Vidyarthi Griha's College of Engineering and Technology and G K Pate(Wani) Institute of Management, Pune :97.56")
    print("INSTITUTE CODE :6274\n")
if a > 97.49:
    print("Vivekanand Education Society's Institute of Technology, Chembur, Mumbai :97.49")
    print("INSTITUTE CODE :3185\n")
if a > 97.26:
    print("K J Somaiya Institute of Engineering and Information Technology, Sion, Mumbai :97.26")
    print("INSTITUTE CODE :3209\n")
if a > 96.83:
    print("Government College of Engineering, Amravati :96.83")
    print("INSTITUTE CODE :1002\n")
if a > 96.56:
    print("Fr. Conceicao Rodrigues College of Engineering, Bandra,Mumba :96.56")
    print("INSTITUTE CODE :3184\n")
if a > 96.36:
    print(" Vidyalankar Institute of Technology,Wadala, Mumbai :96.36")
    print("INSTITUTE CODE :3139\n")
if a > 96.1:
    print(" Agnel Charities' FR. C. Rodrigues Institute of Technology, Vashi, Navi Mumbai :96.1")
    print("INSTITUTE CODE :3197\n")
if a > 95.99:
    print("Pimpri Chinchwad Education Trust's Pimpri Chinchwad College Of Engineering And Research, Ravet :95.99")
    print("INSTITUTE CODE :6822\n")
if a > 95.95:
    print("Government College of Engineering, Nagpur :95.95")
    print("INSTITUTE CODE :4025\n")
if a > 95.52:
    print("MIT Academy of Engineering,Alandi, Pune :95.52")
    print("INSTITUTE CODE :6146\n")
if a > 95.47:
    print("Thakur College of Engineering and Technology, Kandivali, Mumbai :95.47")
    print("INSTITUTE CODE :3176\n")
if a > 95.29:
    print("All India Shri Shivaji Memorial Society's College of Engineering, Pune :95.29")
    print("INSTITUTE CODE :6278\n")
if a > 95.28:
    print(" Dr. D. Y. Patil Pratishthan's D.Y.Patil College of Engineering Akurdi, Pune :95.28")
    print("INSTITUTE CODE :6272\n")
if a > 95.18:
    print("Shri Guru Gobind Singhji Institute of Engineering and Technology, Nanded :95.18")
    print("INSTITUTE CODE :2020\n")
if a > 95.11:
    print("International Institute of Information Technology (I²IT), Pune :95.11")
    print("INSTITUTE CODE :6754\n")
if a > 95.11:
    print("Jaywant Shikshan Prasarak Mandal's,Rajarshi Shahu College of Engineering, Tathawade, Pune :95.11")
    print("INSTITUTE CODE :6141\n")
if a > 94.91:
    print("Don Bosco Institute of Technology, Mumbai :94.91")
    print("INSTITUTE CODE :3208\n")
if a > 94.51:
    print("Manjara Charitable Trust's Rajiv Gandhi Institute of Technology, Mumbai :94.51")
    print("INSTITUTE CODE :3135\n")
if a > 94.44:
    print("Xavier Institute Of Engineering C/O Xavier Technical Institute,Mahim,Mumbai :94.44")
    print("INSTITUTE CODE :3214\n")
if a > 94.35:
    print("St. Francis Institute of Technology,Borivali, Mumbai :94.35")
    print("INSTITUTE CODE :3204")
if a > 94.35:
    print("Government College of Engineering & Research, Avasari Khurd :94.35")
    print("INSTITUTE CODE :6004\n")
if a > 94.34:
    print("S.I.E.S. Graduate School of Technology, Nerul, Navi Mumbai :94.34")
    print("INSTITUTE CODE :3211\n")
if a > 93.96:
    print(" All India Shri Shivaji Memorial Society's Institute of Information Technology,Pune :93.96")
    print("INSTITUTE CODE :6282\n")
if a > 93.57:
    print("Bharati Vidyapeeth's College of Engineering,Lavale, Pune :93.57")
    print("INSTITUTE CODE :6796\n")
if a > 93.49:
    print("Progressive Education Society's Modern College of Engineering, Pune :93.49")
    print("INSTITUTE CODE :6139\n")
if a > 93.48:
    print("Dr. D. Y. Patil Vidya Pratishthan Society’s Dr. D. Y. Patil Institute of Technology, Pimpri, Pune :93.48")
    print("INSTITUTE CODE :6207\n")
if a > 92.95:
    print("Yeshwantrao Chavan College of Engineering,Wanadongri, Nagpur :92.95")
    print("INSTITUTE CODE :4167\n")
if a > 92.68:
    print("Vidyavardhini's College of Engineering and Technology, Vasai :92.68")
    print("INSTITUTE CODE :3194\n")
if a > 92.62:
    print("Marathwada Mitra Mandal's College of Engineering, Karvenagar, Pune :92.62")
    print("INSTITUTE CODE :6156\n")
if a > 92.5:
    print("Bharati Vidyapeeth College of Engineering, Navi Mumbai :92.5")
    print("INSTITUTE CODE :3189\n")
if a > 92.42:
    print("Rizvi Education Society's Rizvi College of Engineering, Bandra,Mumbai :92.42")
    print("INSTITUTE CODE :3201\n")
if a > 92.33:
    print("K. E. Society's Rajarambapu Institute of Technology, Walwa, Sangli :92.33")
    print("INSTITUTE CODE :6214\n")
if a > 92.33:
    print(" Dr. D.Y.Patil Institute of Engineering, Management & Reseach, Akurdi, Pune :92.33")
    print("INSTITUTE CODE :6802\n")
if a > 92.17:
    print("Sinhgad College of Engineering, Vadgaon (BK), Pune :92.17")
    print("INSTITUTE CODE :6177\n")
if a > 92.01:
    print("Shri Sant Gajanan Maharaj College of Engineering,Shegaon :92.01")
    print("INSTITUTE CODE :1101\n")
if a > 91.99:
    print("Shri Sant Gajanan Maharaj College of Engineering,Shegaon :91.99")
    print("INSTITUTE CODE :5121\n")
if a > 91.78:
    print("Kolhapur Institute of Technology's College of Engineering(Autonomous), Kolhapur :91.78")
    print("INSTITUTE CODE :6267\n")
if a > 91.77:
    print("N.Y.S.S.'s Datta Meghe College of Engineering, Airoli, Navi Mumbai :91.77")
    print("INSTITUTE CODE :3187\n")
if a > 91.7:
    print("Government College of Engineering, Jalgaon :91.70")
    print("INSTITUTE CODE :5004\n")
if a > 91.43:
    print("Atharva College of Engineering,Malad(West),Mumbai :91.43")
    print("INSTITUTE CODE :3203\n")
if a > 91.37:
    print("Mahatma Education Society's Pillai College of Engineering, New Panvel :91.37")
    print("INSTITUTE CODE :3207\n")
if a > 91.03:
    print("Mahavir Education Trust's Shah & Anchor Kutchhi Engineering College, Mumbai :91.03")
    print("INSTITUTE CODE :3148\n")
if a > 90.98:
    print("Walchand Institute of Technology, Solapur :90.98")
    print("INSTITUTE CODE :6265\n")
if a > 90.76:
    print("Bharati Vidyapeeth's College of Engineering for Women, Katraj, Dhankawadi, Pune :90.76")
    print("INSTITUTE CODE :6285\n")
if a > 90.62:
    print("Terna Engineering College, Nerul, Navi Mumbai :90.62")
    print("INSTITUTE CODE :3190\n")
if a > 90.28:
    print("Modern Education Society's College of Engineering, Pune :90.28")
    print("INSTITUTE CODE :6281\n")
if a > 89.81:
    print(" Vidya Pratishthan's Kamalnayan Bajaj Institute of Engineering & Technology, Baramati Dist.Pune :89.81")
    print("INSTITUTE CODE :6284\n")
if a > 89.31:
    print("Dattajirao Kadam Technical Education Society's Textile & Engineering Institute, Ichalkaranji :89.31")
    print("INSTITUTE CODE :6222\n")
if a > 89.11:
    print("Amrutvahini Sheti & Shikshan Vikas Sanstha's Amrutvahini College of Engineering, Sangamner :89.11")
    print("INSTITUTE CODE :5162\n")
if a > 89.09:
    print("Shree L.R. Tiwari College of Engineering, Mira Road, Mumbai :89.09")
    print("INSTITUTE CODE :3423\n")
if a > 88.98:
    print("G.H.Raisoni College of Engineering & Management, Wagholi, Pune :88.98")
    print("INSTITUTE CODE :6155\n")
if a > 88.94:
    print("Dr. Babasaheb Ambedkar Technological University, Lonere :88.94")
    print("INSTITUTE CODE :3033\n")
if a > 88.75:
    print("Usha Mittal Institute of Technology SNDT Women's University, Mumbai :88.75")
    print("INSTITUTE CODE :3035\n")
if a > 88.75:
    print("Ankush Shikshan Sanstha's G.H.Raisoni College of Engineering, Nagpur :88.75")
    print("INSTITUTE CODE :4116\n")
if a > 88.66:
    print("Anjuman-I-Islam's M.H. Saboo Siddik College of Engineering, Byculla, Mumbai :88.66")
    print("INSTITUTE CODE :3183\n")
if a > 88.59:
    print("Sinhgad Technical Education Society's Smt. Kashibai Navale College of Engineering,Vadgaon,Pune :88.59")
    print("INSTITUTE CODE :6178\n")
if a > 88.46:
    print(" Maratha Vidya Prasarak Samaj's Karmaveer Adv. Baburao Ganpatrao Thakare College Of Engineering, Nashik :88.46")
    print("INSTITUTE CODE :5108\n")
if a > 88.32:
    print(" JSPM'S Jaywantrao Sawant College of Engineering,Pune :88.32")
    print("INSTITUTE CODE :6145\n")
if a > 87.7:
    print("Sanjivani Rural Education Society's Sanjivani College of Engineering, Kopargaon :87.7")
    print("INSTITUTE CODE :5160\n")
if a > 87.3:
    print("A. P. Shah Institute of Technology, Thane :87.3")
    print("INSTITUTE CODE :3475\n")
if a > 86.83:
    print("Lokmanya Tilak College of Engineering, Kopar Khairane, Navi Mumbai :86.83")
    print("INSTITUTE CODE :3196\n")
if a > 86.79:
    print(" Vasantdada Patil Pratishthan's College Of Engineering and Visual Arts, Sion, Mumbai :86.79")
    print("INSTITUTE CODE :3188\n")
if a > 86.35:
    print("Nutan Maharashtra Vidya Prasarak Mandal, Nutan Maharashtra Institute of Engineering &Technology, Talegaon :86.35")
    print("INSTITUTE CODE :6310\n")
if a > 86.29:
    print("Government College of Engineering,Yavatmal :86.29")
    print("INSTITUTE CODE :1012\n")
if a > 86.23:
    print("Government College of Engineering, Aurangabad :86.23")
    print("INSTITUTE CODE :2008\n")
if a > 86.23:
    print("Smt. Indira Gandhi College of Engineering, Navi Mumbai :86.23")
    print("INSTITUTE CODE :3192\n")
if a > 86.23:
    print(" JSPM's Imperial College of Engineering and Research, Wagholi, Pune :86.23")
    print("INSTITUTE CODE :6160\n")
if a > 86.01:
    print("Saraswati Education Society's Saraswati College of Engineering,Kharghar Navi Mumbai :86.01")
    print("INSTITUTE CODE :3154\n")
if a > 85.83:
    print(" Prof. Ram Meghe Institute of Technology & Research, Amravati :85.83")
    print("INSTITUTE CODE :1105\n")
if a > 85.83:
    print("TSSMS's Pd. Vasantdada Patil Institute of Technology, Bavdhan, Pune :85.83")
    print("INSTITUTE CODE :6122\n")
if a > 85.47:
    print("Saraswati Education Society's Saraswati College of Engineering,Kharghar Navi Mumbai :85.47")
    print("INSTITUTE CODE :6755\n")
if a > 85.05:
    print("Annasaheb Dange College of Engineering and Technology, Ashta, Sangli :85.05")
    print("INSTITUTE CODE :6283\n")
if a > 84.42:
    print("M.G.M.'s College of Engineering and Technology, Kamothe, Navi Mumbai :84.42")
    print("INSTITUTE CODE :3175\n")
if a > 84.42:
    print("Ankush Shikshan Sanstha's G. H. Raisoni Institute of Engineering & Technology, Nagpur :84.42")
    print("INSTITUTE CODE :4142\n")
if a > 84.42:
    print("Shri Vile Parle Kelavani Mandal's Institute of Technology, Dhule :84.42")
    print("INSTITUTE CODE :5449\n")
if a > 84.09:
    print("Indira College of Engineering & Management, Pune :84.09")
    print("INSTITUTE CODE :6179\n")
if a > 84.04:
    print(" Jawahar Education Society's Annasaheb Chudaman Patil College of Engineering,Kharghar, Navi Mumbai :84.09")
    print("INSTITUTE CODE :3146\n")
if a > 84.01:
    print(" D.Y. Patil College of Engineering and Technology, Kolhapur :84.01")
    print("INSTITUTE CODE :6250\n")
if a > 83.98:
    print("Sinhgad Technical Education Society, Sinhgad Institute of Technology and Science, Narhe (Ambegaon) :83.98")
    print("INSTITUTE CODE :6182\n")
if a > 83.51:
    print("G. S. Mandal's Maharashtra Institute of Technology, Aurangabad :83.51")
    print("INSTITUTE CODE :2113\n")
if a > 83.44:
    print("Excelsior Education Society's K.C. College of Engineering and Management Studies and Research, Kopri, Thane (E) :83.44")
    print("INSTITUTE CODE :3210\n")
if a > 83.08:
    print(" Pravara Rural College of Engineering, Loni, Pravaranagar, Ahmednagar :83.08")
    print("INSTITUTE CODE :5139\n")
if a > 83.08:
    print("NBN Sinhgad Technical Institutes Campus, Pune :83.08")
    print("INSTITUTE CODE :6772\n")
if a > 83.07:
    print("MET Bhujbal Knowledge City MET League's Engineering College, Adgaon, Nashik :83.07")
    print("INSTITUTE CODE :5151\n")
if a > 83.07:
    print("Dr. D. Y. Patil School OF Engineering, Lohegaon, Pune :83.07")
    print("INSTITUTE CODE :6732\n")
if a > 82.77:
    print(" Deogiri Institute of Engineering and Management Studies, Aurangabad :82.77")
    print("INSTITUTE CODE :2114\n")
if a > 82.17:
    print(" Aldel Education Trust's St. John College of Engineering & Management, Vevoor, Palghar :82.17")
    print("INSTITUTE CODE :3218\n")
if a > 81.98:
    print("Aldel Education Trust's St. John College of Engineering & Management, Vevoor, Palghar :81.98")
    print("INSTITUTE CODE :3471\n")
if a > 81.98:
    print("Zeal Education Society's Zeal College of Engineering & Reserch, Narhe, Pune :81.98")
    print("INSTITUTE CODE :6298\n")
if a > 81.64:
    print("Sinhgad Academy of Engineering, Kondhwa (BK) Kondhwa-Saswad Road, Pune :81.64")
    print("INSTITUTE CODE :6187\n")
if a > 81.64:
    print("Sir Shantilal Badjate Charitable Trust's S. B. Jain Institute of technology, Management & Research, Nagpur :81.67")
    print("INSTITUTE CODE :4137\n")
if a > 81.61:
    print(" Marathwada Mitra Mandal's Institute of Technology, Lohgaon, Pune :81.61")
    print("INSTITUTE CODE :6203\n")
if a > 81.29:
    print("Lokmanya Tilak Jankalyan Shikshan Sanstha, Priyadarshani College of Engineering, Nagpur :81.29")
    print("INSTITUTE CODE :4123\n")
if a > 80.76:
    print(" Shivajirao S. Jondhale College of Engineering, Dombivali,Mumbai :80.76")
    print("INSTITUTE CODE :3193\n")
if a > 80.55:
    print("Tatyasaheb Kore Institute of Engineering and Technology, Warananagar :80.55")
    print("INSTITUTE CODE :6268\n")
if a > 80.39:
    print(" Jayawant Shikshan Prasarak Mandal, Bhivarabai Sawant Institute of Technology & Research, Wagholi :80.39")
    print("INSTITUTE CODE :6311\n")
if a > 80.23:
    print(" R. C. Patel Institute of Technology, Shirpur :80.23")
    print("INSTITUTE CODE :5172\n")
if a > 80.22:
    print("Bajaj Institute of Technology, Wardha :80.22")
    print("INSTITUTE CODE :4649\n")
if a > 80.22:
    print("ISBM College Of Engineering Pune :80.22")
    print("INSTITUTE CODE :6622\n")
if a > 79.95:
    print("Pradnya Niketan Education Society's Nagesh Karajagi Orchid College of Engineering & Technology, Solapur :79.95")
    print("INSTITUTE CODE :6223\n")
if a > 79.65:
    print("Dr. D. Y. Patil School of Engineering & Technology, Charholi(Bk), Via Lohgaon, Pune :79.65")
    print("INSTITUTE CODE :6786\n")
if a > 79.54:
    print("TSSM's Bhivarabai Sawant College of Engineering and Research, Narhe, Pune :79.54")
    print("INSTITUTE CODE :6649\n")
if a > 79.3:
    print("Government College of Engineering, Chandrapur :79.30")
    print("INSTITUTE CODE :4004\n")
if a > 79.25:
    print("Mahatma Education Society's Pillai HOC College of Engineering & Technology, Tal. Khalapur. Dist. Raigad :79.25")
    print("INSTITUTE CODE :3223\n")
if a > 78.86:
    print("Sipna Shikshan Prasarak Mandal College of Engineering & Technology, Amravati :78.86")
    print("INSTITUTE CODE :1114\n")
if a > 78.58:
    print("Leela Education Society, G. V. Acharya Polytechnic,Shelu, Karjat :78.58")
    print("INSTITUTE CODE :3221\n")
if a > 78.51:
    print("Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded :78.51")
    print("INSTITUTE CODE :2127\n")
if a > 78.43:
    print("Rasiklal M. Dhariwal Sinhgad Technical Institutes Campus, Warje, Pune :78.43")
    print("INSTITUTE CODE :6769\n")
if a > 78.09:
    print(" Shetkari Shikshan Mandal's Pad. Vasantraodada Patil Institute of Technology, Budhgaon, Sangli :78.09")
    print("INSTITUTE CODE :6269\n")
if a > 78.09:
    print("Gokhale Education Society's, R.H. Sapat College of Engineering, Management Studies and Research, Nashik :78.09")
    print("INSTITUTE CODE :5181\n")
if a > 78.09:
    print("Anjuman-I-Islam's Kalsekar Technical Campus, Panvel :78.09")
    print("INSTITUTE CODE :3439\n")
if a > 77.8:
    print("Shri Vithal Education and Research Institute's College of Engineering, Pandharpur :77.80")
    print("INSTITUTE CODE :6220\n")
if a > 77.8:
    print(" Shivnagar Vidya Prasarak Mandal's College of Engineering, Malegaon-Baramati :77.80")
    print("INSTITUTE CODE :6275\n")
if a > 77.61:
    print("Dhole Patil Education Society, Dhole Patil College of Engineering, Wagholi, Tal. Haveli :77.61")
    print("INSTITUTE CODE :6307\n")
if a > 77.61:
    print(" Bharati Vidyapeeth's College of Engineering, Kolhapur :77.61")
    print("INSTITUTE CODE :6288\n")
if a > 77.53:
    print(" Hope Foundation and research center's Finolex Academy of Management and Technology, Ratnagiri :77.53")
    print("INSTITUTE CODE :3200\n")
if a > 77.38:
    print("Pune District Education Association's College of Engineering, Pune :77.38")
    print("INSTITUTE CODE :6206\n")
if a > 77.35:
    print("Sharad Institute of Technology College of Engineering, Yadrav(Ichalkaranji) :77.35")
    print("INSTITUTE CODE :6317\n")
if a > 77.35:
    print("Sandip Foundation, Sandip Institute of Technology and Research Centre, Mahiravani, Nashik :77.35")
    print("INSTITUTE CODE :5109\n")
if a > 77.35:
    print("Priyadarshini Bhagwati College of Engineering, Harpur Nagar, Umred Road,Nagpur :77.35")
    print("INSTITUTE CODE :4177\n")
if a > 77.31:
    print(" Gharda Foundation's Gharda Institute of Technology,Khed, Ratnagiri :77.31")
    print("INSTITUTE CODE :3216\n")
if a > 77.31:
    print("S K N Sinhgad College of Engineering, Korti Tal. Pandharpur Dist Solapur :77.31")
    print("INSTITUTE CODE :6643\n")
if a > 76.75:
    print("M.S. Bidve Engineering College, Latur :76.75")
    print("INSTITUTE CODE :2129\n")
if a > 76.75:
    print("KJEI's Trinity Academy of Engineering, Yewalewadi, Pune :76.75")
    print("INSTITUTE CODE :6634\n")
if a > 76.23:
    print(" WATUMULL INSTITUTE OF ELECTRONICS ENGINEERING & COMPUTER TECHNOLOGY, ULHASNAGAR :76.23")
    print("INSTITUTE CODE :3212\n")
if a > 76.15:
    print("Rayat Shikshan Sanstha's Karmaveer Bhaurao Patil College of Engineering, Satara :76.15")
    print("INSTITUTE CODE :6270\n")
if a > 76.15:
    print("K. J.'s Educational Institut Trinity College of Engineering and Research, Pisoli, Haveli :76.15")
    print("INSTITUTE CODE :6184\n")
if a > 75.9:
    print(" Lokmanya Tilak Jankalyan Shikshan Sastha, Priyadarshini J. L. College Of Engineering, Nagpur :75.90")
    print("INSTITUTE CODE :4136\n")
if a > 75.43:
    print(" P. R. Pote (Patil) Education & Welfare Trust's Group of Institution(Integrated Campus), Amravati :75.43")
    print("INSTITUTE CODE :1107\n")
if a > 75.1:
    print("Chhartrapati Shivaji Maharaj Institute of Technology, Shedung, Panvel :75.10")
    print("INSTITUTE CODE :3477\n")
if a > 75.1:
    print("Anantrao Pawar College of Engineering & Research, Pune :75.10")
    print("INSTITUTE CODE :6794\n")
if a > 75.05:
    print("SNJB's Late Sau. Kantabai Bhavarlalji Jain College of Engineering, (Jain Gurukul), Neminagar,Chandwad,(Nashik) :75.05")
    print("INSTITUTE CODE :5173\n")
if a > 74.58:
    print("N. B. Navale Sinhgad College of Engineering, Kegaon, solapur :74.58")
    print("INSTITUTE CODE :6640\n")
if a > 74.35:
    print("Jaidev Education Society, J D College of Engineering and Management, Nagpur :74.35")
    print("INSTITUTE CODE :4138\n")
if a > 74.25:
    print("Genba Sopanrao Moze Trust Parvatibai Genba Moze College of Engineering,Wagholi, Pune :74.25")
    print("INSTITUTE CODE :6138\n")
if a > 74.25:
    print("Prof Ram Meghe College of Engineering and Management, Badnera :74.25")
    print("INSTITUTE CODE :1128\n")
if a > 73.96:
    print("PUNE VIDYARTHI GRIHA’S COLLEGE OF ENGINEERING & SHRIKRUSHNA S. DHAMANKAR INSTITUTE OF MANAGEMENT, :73.96")
    print("INSTITUTE CODE :5330\n")
if a > 73.81:
    print("Dr. J. J. Magdum Charitable Trust's Dr. J.J. Magdum College of Engineering, Jaysingpur :73.81")
    print("INSTITUTE CODE :6277\n")
if a > 73.81:
    print("Department of Technology, Shivaji University, Kolhapur :73.81")
    print("INSTITUTE CODE :6028\n")
if a > 73.81:
    print("Cummins College of Engineering For Women, Sukhali (Gupchup), Tal. Hingna Hingna Nagpur :73.81")
    print("INSTITUTE CODE :4304\n")
if a > 73.64:
    print("Sandip Foundation's, Sandip Institute of Engineering & Management, Nashik :73.64")
    print("INSTITUTE CODE :5331\n")
if a > 72.89:
    print("Gramodyogik Shikshan Mandal's Marathwada Institute of Technology, Aurangabad :72.89")
    print("INSTITUTE CODE :2126\n")
if a > 72.89:
    print("Dr.D.Y.Patil College Of Engineering & Innovation,Talegaon :72.89")
    print("INSTITUTE CODE :6834\n")
if a > 72.65:
    print("Lokmanya Tilak Jankalyan Shikshan Sanstha's , Priyadarshini Institute of Engineering and Technology, Nagpur :72.65")
    print("INSTITUTE CODE :4171\n")
if a > 72.65:
    print(" K.D.K. College of Engineering, Nagpur :72.65")
    print("INSTITUTE CODE :4147\n")
if a > 72.65:
    print("Sinhagad Institute of Technology, Lonavala :72.65")
    print("INSTITUTE CODE :6185\n")
if a > 72.57:
    print("Vishwaniketan's Institute of Management Entrepreneurship and Engineering Technology(i MEET), Khalapur :72.57")
    print("INSTITUTE CODE :3467\n")
if a > 72.46:
    print("Nutan College of Engineering and Research, Talegaon Dabhade Tal. Maval, Pune :72.46")
    print("INSTITUTE CODE :6419\n")
if a > 72.28:
    print("Konkan Gyanpeeth College of Engineering, Karjat :72.28")
    print("INSTITUTE CODE :3198\n")
if a > 72.28:
    print("Dr. Ashok Gujar Technical Institute's Dr. Daulatrao Aher College of Engineering, Karad :72.28")
    print("INSTITUTE CODE :6303\n")
if a > 72.12:
    print("CSMSS Chh. Shahu College of Engineering, Aurangabad :72.12")
    print("INSTITUTE CODE :2533\n")
if a > 70.82:
    print("Guru Gobind Singh College of Engineering & Research Centre, Nashik. :70.82")
    print("INSTITUTE CODE :5418\n")
if a > 70.82:
    print("Mauli Group of Institutions, College of Engineering and Technology, Shegaon. :70.82")
    print("INSTITUTE CODE :1265\n")
if a > 70.39:
    print("Dr. D Y Patil Pratishthan's College of Engineering, Kolhapur :70.39")
    print("INSTITUTE CODE :6839\n")
if a > 70.39:
    print("S.S.P.M.'s College of Engineering, Kankavli :70.39")
    print("INSTITUTE CODE :3206\n")
if a > 70.39:
    print(" Shri Shivaji Vidya Prasarak Sanstha's Late Bapusaheb Shivaji Rao Deore College of Engineering,Dhule :70.39")
    print("INSTITUTE CODE :5103\n")
if a > 69.66:
    print("Keystone School of Engineering, Pune :69.66")
    print("INSTITUTE CODE :6808\n")
if a > 69.31:
    print("Shramsadhana Bombay Trust, College of Engineering & Technology, Jalgaon :69.31")
    print("INSTITUTE CODE :5104\n")
if a > 69.31:
    print("Shri Hanuman Vyayam Prasarak Mandals College of Engineering & Technology, Amravati :69.31")
    print("INSTITUTE CODE :1121\n")
if a > 68.99:
    print("Genba Sopanrao Moze College of Engineering, Baner-Balewadi, Pune :68.99")
    print("INSTITUTE CODE :6144\n")
if a > 68.32:
    print("Kavi Kulguru Institute of Technology & Science, Ramtek :4104")
    print("INSTITUTE CODE :4104\n")
if a > 68.1:
    print(" Universal College of Engineering & Research, Sasewadi :68.10")
    print("INSTITUTE CODE :6625\n")
if a > 67.77:
    print("Saraswati Education Society, Yadavrao Tasgaonkar Institute of Engineering & Technology, Karjat :67.77")
    print("INSTITUTE CODE :3147\n")
if a > 67.77:
    print("Sant Gajanan Maharaj College of Engineering, Gadhinglaj :67.77")
    print("INSTITUTE CODE :6803\n")
if a > 67.69:
    print("Suryodaya College of Engineering & Technology, Nagpur :67.69")
    print("INSTITUTE CODE :4613\n")
if a > 66.75:
    print("Vighnaharata Trust's Shivajirao S. Jondhale College of Engineering & Technology, Shahapur, Asangaon, Dist Thane :66.75")
    print("INSTITUTE CODE :3217\n")
if a > 65.8:
    print("Jawaharlal Darda Institute of Engineering and Technology, Yavatmal :65.80")
    print("INSTITUTE CODE :1120\n")
if a > 65.33:
    print(" Jaihind College Of Engineering,Kuran :65.33")
    print("INSTITUTE CODE :6609\n")
if a > 64.16:
    print("Matoshri College of Engineering and Research Centre, Eklahare, Nashik :64.16")
    print("INSTITUTE CODE :5177\n")
if a > 64.03:
    print("Shri. Sai Shikshan Sanstha, Nagpur Institute of Technology, Nagpur :64.03")
    print("INSTITUTE CODE :4144\n")
if a > 63.71:
    print("D.Y.Patil Education Society's,D.Y.Patil Technical Campus, Faculty of Engineering & Faculty of Management,Talsande :63.71")
    print("INSTITUTE CODE :6780\n")
if a > 63.69:
    print(" Rajendra Mane College of Engineering & Technology Ambav Deorukh :63.69")
    print("INSTITUTE CODE :3202\n")
if a > 63.65:
    print("Ahmednagar Jilha Maratha Vidya Prasarak Samajache, Shri. Chhatrapati Shivaji Maharaj College of Engineering :63.65")
    print("INSTITUTE CODE :5382\n")
if a > 63.65:
    print("deal Institute of Technology, Wada, Dist.Thane :63.65")
    print("INSTITUTE CODE :3465\n")
if a > 61.52:
    print("G. H. Raisoni Institute of Business Management,Jalgaon :61.52")
    print("INSTITUTE CODE :5152\n")
if a > 61.25:
    print(" Nanasaheb Mahadik College of Engineering,Walwa, Sangli :61.25")
    print("INSTITUTE CODE :6762\n")
if a > 59.78:
    print(" Dnyanshree Institute engineering and Technology, Satara :59.78")
    print("INSTITUTE CODE :6797\n")
if a > 58.61:
    print("Kai Amdar Bramhadevdada Mane Shikshan & Samajik Prathistan's Bramhadevdada Mane Institute of Technology solapur :58.61")
    print("INSTITUTE CODE :6293\n")
if a > 57.24:
    print("Paramhansa Ramkrishna Maunibaba Shikshan Santha's , Anuradha Engineering College, Chikhali :57.24")
    print("INSTITUTE CODE :1119\n")
if a > 53.51:
    print("Samarth Education Trust's Arvind Gavali College Of Engineering Panwalewadi, Varye,Satara. :53.51")
    print("INSTITUTE CODE :6545\n")
if a > 47.89:
    print("Vidya Prasarini Sabha's College of Engineering & Technology, Lonavala :47.89")
    print("INSTITUTE CODE :6815\n")
if a > 37.56:
    print("Vishvatmak Jangli Maharaj Ashram Trust's Vishvatmak Om Gurudev College of Engineering, Mohili-Aghai, Shahpur :37.56")
    print("INSTITUTE CODE :3445\n")
else:
    print("SORRY, WE CAN'T FIND ANY RESULT !!!")

print("Thank You For Visiting US!!!!  ")

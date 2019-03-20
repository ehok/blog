Mert Öngengil 15253041


    Docker Yükleme Adımları

        ~ sudo apt update
        ~ sudo apt install apt-transport-https ca-certificates curl software-properties-common
        ~ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        ~ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
        ~ sudo apt update
        ~ apt-cache policy docker-ce
        ~ sudo apt install docker-ce
        ~ sudo usermod -aG docker ${USER}
        ~ su - ${USER}
        ~ sudo usermod -aG docker Kullanıcı_Adı

    Docker-Compose Yükleme Adımları

        ~ sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        ~ sudo chmod +x /usr/local/bin/docker-compose

    Projeyi Çalıştırma

        ~ Proje dizininde "sudo docker-compose up -d" komutu çalıştırılır



    Ödev 2 için

        pgadmin ile veritabanını güncelleyebilirsiniz. ("username:postgres","password:postgres","port:5432")

        DES algoritmasını kullandım. Kendi seçtiğim key '01234567' dir. DES algoritmasını kullanabilmek için padding yapmam gerekti. 
        Sebebi ise metnimin uzunlugunun 8'in katı olmasını sağlamak.


    Ödev 3 için

        Rastgele dağılım başarılı olması için numpy modülünü kullandım. Frekans analizi için ise 
        rastgele metini oluştururken harflerden oluşan ordered dictionary nin deger kısmında tekrar sayılarını tuttum.
        Ve analiz edebilmek için standart sapmasını hesaplayarak yazdırdım. 
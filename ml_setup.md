Jeśli są jakieś niejasności można się skontaktować na discord: `domin._`

## Google Colab
W czasie wakacyjnego kursu będziemy głównie operować na notatnikach Jupyter na platformie Google Colab (jeśli nie masz jeszcze konta na googlu to pora założyć). Więc warto byłoby się zapoznać jak taki notatnik przygotować:

### Stworzenie notatnika
Wchodząc na strone: https://colab.research.google.com powinniśmy zostać przywitani taką stroną:


![alt text](<screenshots/Screenshot 2025-07-26 at 01.25.55.png>)

Możesz zauważyć, ze podstawowo przy pierwszym logowaniu Google Colab oferuje nam poradnik jak korzystać z takowych notatników na ich platformie. Jeśli jesteś zainteresowany co dokładnie nam ta platforma oferuje, mozesz śmiało przeczytać ten poradnik. Ale nas interesuje stworzenie nowego notatnika, kliknij `New notebook`. W ten oto sposób utworzyłeś nowy notatnik, na którym będziesz mógł pracować.

> Jeśli z jakiegoś powodu nie pokazało Ci się okno `Open Notebook`, nowy notebook możesz zrobić poprzez kliknięcie `File -> New Notebook` in Drive.

### Uzywanie notatnika
Po stworzeniu notatnika, Google Colab stworzy nam segment kodu na którym możemy testować nasz kod i odpalać program.

![alt text](<screenshots/Screenshot 2025-07-26 at 01.38.54.png>)

> Możesz zauwazyć, że ostatnia linijka w segmencie kodu, działa tak jak print 🔥

Zeby dodać kolejne segmenty kodu wystarczy najechać myszką pod segment kodu i pojawi nam się:

![alt text](<screenshots/Screenshot 2025-07-26 at 01.44.57.png>)

Można także dodawać komentarze markdown, które są bardzo przydatne przy opisywaniu co się w danym segmencie kodu dzieje:

![alt text](<screenshots/Screenshot 2025-07-26 at 01.48.13.png>)

Dużą zaletą takiego notatnika, jest to że odpalony wcześniej segment kodu działa wobec innych segmentów kodu (zachowuje kontekst), więc możemy testować kod fragmentami:

![alt text](<screenshots/Screenshot 2025-07-26 at 02.04.55.png>)

zmienne X i Y, które zostały zdefiniowane wcześniej działają dla nowego segmentu!

### Importowanie bibliotek w notatniku

Nie raz będziemy potrzebowali zaimportować jakąś libke w notatniku (Google Colab ma już wgrane w środowisko dużo przydatnych bibliotek), ale tutaj przecież nie ma zadnego terminala, żeby uzyć pip install, w notatniku jupytera robimy to wewnątrz segmentu kodu:

![alt text](<screenshots/Screenshot 2025-07-26 at 01.56.11.png>)

W notatniku Jupyter:
- wykrzyknik umożliwia wykonanie polecenia systemowego (shellowego) z poziomu komórki notebooka (działa jak wpisanie komendy w terminalu)
- to są tak zwane "magic commands", czyli specjalne polecenia Jupyter Notebooka, które dają dodatkowe  (jeśli jesteś ciekawy co oferuje Jupyter Notebook możesz wpisać w kodzie `%lsmagic`, żeby wyprintować wszystkie metody).

### Ustawienia notatnika
Wchodząc w Edit -> Notebook Settings, możecie między innymi przestawić wykonywanie programu z CPU na GPU, jeśli chcecie i także schować podpowiadanie kodu przez AI

![alt text](<screenshots/Screenshot 2025-07-26 at 02.07.03.png>)

### Ładowanie stworzonego juz notatnika
Jeśli wchodzicie znowu na strone Google Colab i chcecie dokończyć robote co zostawiliście sobie na później, na ekranie startowym dostaniecie automatycznie skąd chcecie odpalić poprzedni notebook

![alt text](<screenshots/Screenshot 2025-07-26 at 02.09.38.png>)

a jak chcecie się przełączyć z jednego notebooka na drugi to poprzez `File -> Open notebook` i dostaniecie to samo okno.

## GitHub
W ramach tego kursu będziecie mieć własnego brancha `dev` na repozytorium kursu, który wam wygenerujemy, na nim będziecie przesyłać swoje rozwiązania zadań i z poziomu swojego brancha będziecie tworzyć pull request na maina, jedyne co będziecie musieli zrobić to przypisać się jako assignee, a my wam przydzielimy reviewerów zadania, jak i zamkniemy pull request przy podanym przez nas terminie po zakończeniu review.

### 1. Pobierz notebook z maina z GitHuba

1. Wejdź na repozytorium na GitHubie.
2. Przejdź do branch `main`.
3. Znajdź interesujący Cię plik notebooka (`.ipynb`).

![alt text](<screenshots/Screenshot 2025-07-29 at 18.22.44.png>)

4. Kliknij na plik, a potem na przycisk **Raw**.

![alt text](<screenshots/Screenshot 2025-07-29 at 18.26.58.png>)

5. Skopiuj adres URL z paska przeglądarki.

### 2. Importuj notebook w Google Colab

1. Otwórz [Google Colab](https://colab.research.google.com/).
2. Wybierz **File** > **Open notebook**.
3. Przejdź do zakładki **GitHub**.
4. Wklej wcześniej skopiowany URL pliku notebooka z GitHuba.

![alt text](<screenshots/Screenshot 2025-07-29 at 18.24.48.png>)

5. Kliknij **Search** (Szukaj), a następnie wybierz swój plik i kliknij na niego. Wtedy powinien otworzyć Ci się notebook

_Alternatywnie_: możesz wybrać **File > Open notebook > Upload** i załadować notebook pobrany z komputera.

### 3. Podepnij Dysk Google w Colabie

1. W Colabie wklej poniższy kod w nową komórkę i uruchom ją:

    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```

2. Daj potrzebne permisje google colabowi, po daniu permisji:
![alt text](<screenshots/Screenshot 2025-07-29 at 18.35.42.png>)

Po tym powinieneś móc pod tą ścieżką wylistować wszystkie swoje pliki w dysku `%ls /content/drive/MyDrive`

### 4. Wgraj dane na swój Dysk Google
1. Wejdź na [Google Drive](https://drive.google.com/).
2. Przeciągnij plik/dane do odpowiedniego folderu na Dysku.
3. Następnie w notebooku możesz odwołać się do tego pliku np.:

    ```python
    data_path = '/content/drive/MyDrive/nazwa_folderu/nazwa_pliku.csv'
    ```

### 5. Pracuj w notatniku, dokonaj potrzebnych zmian

- Wykonaj analizy/kod zgodnie z zadaniem.

### 6. Pobierz skończony notatnik

1. W Colabie wybierz **File (Plik) > Download > Download .ipynb** (Pobierz jako .ipynb).
2. Plik zostanie zapisany na Twoim komputerze.

### 7. Wgraj notatnik na SWOJEGO brancha `dev` w repozytorium GitHub
1. Kliknij **Add file > Upload files** i wybierz pobrany plik notebooka.

![alt text](<screenshots/Screenshot 2025-07-29 at 18.34.13.png>)

2. Zatwierdź zmiany (commit).

### 8. Stwórz Pull Request
1. Po wgraniu zmian pojawi się propozycja utworzenia Pull Requesta.
2. Kliknij **Compare & pull request**.
3. Uzupełnij opis, upewnij się, że porównywane są właściwe gałęzie, zmiany powinny zostać wprowadzone na SWOJEGO `main` (`user-dev` → `user-main`).
4. Kliknij **Create pull request**.

### Pull requesty
Tutaj przedstawimy prostą mechanike jak można stworzyć pull request na dowolnym repozytorium.

Załóżmy, że mamy takie o to repozytorium:

![alt text](<screenshots/Screenshot 2025-07-26 at 18.26.19.png>)

Wchodząc w zakładke pull requests klikamy `New Pull Request` i przejdziemy na stronę, gdzie możemy porównać naszego brancha z jakimś innym (na tym przykładzie zrobimy pull request na main):

![alt text](<screenshots/Screenshot 2025-07-26 at 18.29.57.png>)

> Base przy porównywaniu to jest branch, w którym chcemy wprowadzić zmiany (`main`) a compare to branch, z którego pochodzą zmiany (`dev`).

I następnie klikamy `Create pull request`

![alt text](<screenshots/Screenshot 2025-07-26 at 18.32.54.png>)

Przy pull requeście możemy wybrać kto będzie robił recenzje danych zmian i możemy także przypisać osobę odpowiedzialną za wykonanie (klikając zębatke przy reviewers i assignee odpowiednio). Kiedy stworzymy już adekwatny tytuł i opis oraz przypiszemy osoby do pull requestu klikamy `Create pull request`.

Kiedy już stoi taki pull request czekamy od osób trzeci na adekwatny roast zmian/nowych feature'ów.

Teraz, w jaki sposób możemy jakiejś osobie zrobić recenzje? W naszym repozytorium w zakładce Pull Requests, możemy zauważyć, wszystkie aktywne pull requesty na repozytorium:

![alt text](<screenshots/Screenshot 2025-07-26 at 18.39.22.png>)

Wchodząc w interesujący nas pull request, mamy opcje:
- Napisanie prostego komentarza:

![alt text](<screenshots/Screenshot 2025-07-26 at 18.41.06.png>)

Ale także komentarze, które odnoszą się do jakiegoś kawałka kodu, możemy to zrobić poprzez wejście w zakładke przy pull requeście `Files Changed` i klikając interesującą nas linijke: 

![alt text](<screenshots/Screenshot 2025-07-26 at 18.45.52.png>)

i kliknąć `Start a review`. Wtedy na głównej stronie pull requestu pojawi się:

![alt text](<screenshots/Screenshot 2025-07-26 at 18.46.56.png>)

Jako iż w pull request jupyter notebooki są pokazywane jakby w formacie jsona, dobrym pomysłem jest przejście z pull requesta na faktyczny notebook i tam na niego spojrzeć i w pull request napisać normalny komentarzy (nie koniecznie zaznaczając fragment jsona).

<img width="628" height="520" alt="Screenshot 2025-08-01 at 16 49 36" src="https://github.com/user-attachments/assets/c56ed21f-a829-49e3-a34c-e61fc8d1ae2b" />

Ostatecznie jeśli wszystko zostało rozwiązane czy to jakiś konflikt czy jakieś zrequestowane zmiany w kodzie osoba która robi approve i klika `Merge Pull Request` i w ten oto sposób zmiany z brancha zostały wrzucone na main.

## Discord

<h1>Pierwsza strona w PHP</h1>

<?php //znacznik otwierajcy skrypt php
  // phpinfo();
   //znacznik zamykajacy skrypt php
   print_r($_POST);
 ?>

<form name="formularz" id="formularz" method="POST">
    <table class="table">
      <tr>
        <td><label for="imie">Imię:</label></td>
        <td><input type="text" name="imie" value=""></td>
      </tr>
      <tr>
        <td><label for="nazwisko">Nazwisko:</label></td>
        <td><input type="text" name="nazwisko" value=""></td>
      </tr>

    </table>

    <fieldset>

      <legend>Wybierz płeć:</legend>
        <input type="radio" name="gender" value="mezczyzna" > Mezczyzna<br>
        <input type="radio" name="gender" value="kobieta"> Kobieta<br>
        <input type="radio" name="gender" value="inna" checked> inna

    </fieldset>
      <fieldset>
        <legend>Wybierz pojazd:</legend>
          <input type="checkbox" name="vehicle1" value="Bike"> I have a bike<br>
          <input type="checkbox" name="vehicle2" value="Car"> I have a car
      </fieldset>
      <select name="cars">
        <option value="volvo">Volvo</option>
        <option value="saab">Saab</option>
        <option value="fiat">Fiat</option>
        <option value="audi" selected>Audi</option>
      </select>
      <select name="cars2" multiple>
        <option value="volvo">Volvo</option>
        <option value="saab">Saab</option>
        <option value="fiat">Fiat</option>
        <option value="audi" selected>Audi</option>
      </select>

<br>
<textarea name="message" rows="10" cols="30">
HEHEHEHEHHEHE XD
</textarea>
<br>
    <input type="submit" name="" value="Prześlij">
    <input type="reset" name="" value="Resetuj">

</form>

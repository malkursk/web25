// функция для вычисления суммы
function calculateSum(x, y){
    return x + y;
  }
  
  // Обновите код в фукнции calculateSum, чтобы следующие выражения работали ожидаемым образом
  console.log(calculateSum(10, '10'));  // 20
  console.log(calculateSum('5', '10')); // 15
  console.log(calculateSum(8, 8.8));  // 16.8
  
  
  // функция для получения рекомендаци по погоде
  function getWeatherRecommendations(isSunny, isRainy, isSnowy) {
    console.log('Дождь, нужен зонт.');
    console.log('Солнце, нужен крем');
    console.log('Снег, нужна шапка');
    console.log('Снег и солнце, нужны очки');
    console.log('Просто хороший день');
  }
  
  // Используйте условные операторы в функции выше, чтобы  выражения работали адекватно
  getWeatherRecommendations(true, false, false);  // Солнце, нужен крем
  getWeatherRecommendations(false, true, false);  // Дождь, нужен зонт
  getWeatherRecommendations(true, false, true);  // Снег и солнце, нужны очки
  getWeatherRecommendations(false, false, true);  // Снег, нужна шапка
  getWeatherRecommendations(false, false, false);  // Просто хороший день
  
  
  // Функция для проверки значения на false, измените функцию таким образом, 
  // чтобы только переменна boolean типа со значением false давала результат "Значение равно false"
  function checkIfValIsFalse(value) {
      if (value == false) {
        console.log("Значение равно false");
    } else {
        console.log("Значение не равно false");
    }
  }
  
  checkIfValIsFalse(false); // "Значение равно false"
  checkIfValIsFalse(0); // "Значение не равно false"
  checkIfValIsFalse(''); // "Значение не равно false"
  checkIfValIsFalse(null); // "Значение не равно false"
  
  
  // Функция для демонстрации работы со строками
  function stringOperations() {
      let greeting = "Hello, world!";
  
      // Вывод длины строки
      console.log(`Длина строки: ???`);
  
      // Получение символа строки по индексу
      console.log(`Символ по индексу 1: ???`);
  
      // Преобразование строки в верхний регистр
      console.log(`Строка в верхнем регистре: ???`);
  
      // Поиск подстроки в строке
      let searchTerm = "world";
  
      /// напишите код, который будет выводить "Строка содержит подстроку <searchTerm>" если searchTerm есть в greeting
      
      let firstName = "Данила";
      let middleName = "Ярославович";    
      let lastName = "Пешков";
      console.log(`Полное имя: ??? ??? ???`);
  
      // получите четвертое слово из строки "Мы учимся на цифровой кафедре в ЮЗГУ"
      // let subString = ???
      //console.log(`Подстрока: ${subString}`);
  }
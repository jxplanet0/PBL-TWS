$(document).ready(function () {
  const $ = jQuery;
  $('nav.navbar').addClass('navbar-active');
  $(".navbar-nav .nav-link").hover(
    function () {
      $(this).css("color", "#007bff");
    },
    function () {
      $(this).css("color", "#333");
    }
  );

  $(".username-label").hover(
    function () {
      $(this).css("color", "#007bff");
    },
    function () {
      $(this).css("color", "#333");
    }
  );
});
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

$(document).ready(function() {
  $('#search-form').on('submit', function(event) {
    event.preventDefault();
    var searchValue = $('#search-form input').val();
    var names = $('#name-filter').val();
    var ram = $('#ram-filter').val();
    var storage_capacity = $('#storage_capacity-filter').val();
    var processor_brand = $('#processor_brand-filter').val();
    var graphic = $('#graphic-filter').val();
    var price = $('#price-filter').val();
    searchLaptops(searchValue, names, ram, storage_capacity, processor_brand, graphic, price);
  });

  function searchLaptops(searchValue, name, ram, storage_capacity, processor_brand, graphic, price) {
    $.ajax({
      type: "POST",
      url: "/Tampilan Web/backend/searchlaptop.php",
      data: {
        searchValue: searchValue,
        name: name,
        ram: ram,
        storage_capacity: storage_capacity,
        processor_brand: processor_brand,
        graphic: graphic,
        price: price
      },
      dataType: "json",
      success: function(data) {
        displaySearchResults(data);
      }
    });
  }

  function displaySearchResults(data) {
    let searchResults = document.getElementById('search-results');
    searchResults.innerHTML = '';

    data.forEach(function(laptop) {
      let laptopDiv = document.createElement('div');
      laptopDiv.className = 'laptop';
      laptopDiv.innerHTML = `
        <h2>${laptop.name}</h2>
        <p>name: ${laptop.name}</p>
        <p>CPU: ${laptop.cpu}</p>
        <p>RAM: ${laptop.ram} GB</p>
        <p>storage_capacity: ${laptop.storage_capacity} GB</p>
        <p>graphic: ${laptop.graphic}</p>
        <p>Harga: ${laptop.price}</p>
      `;
      searchResults.appendChild(laptopDiv);
    });
  }
});
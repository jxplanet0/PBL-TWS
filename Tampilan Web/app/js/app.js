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
$(document).ready(function() {
  $('.btn-submit').on('click', function(event) {
    event.preventDefault(); 
    var searchValue = $('.search-bar input').val();
    var searchResults = searchLaptops(searchValue); 
    displaySearchResults(searchResults);
  });

  function searchLaptops(searchValue) {
    var laptops = [
      { name: "Laptop A", specs: "Specs A", price: "$1000" },
      { name: "Laptop B", specs: "Specs B", price: "$1200" },
      { name: "Laptop C", specs: "Specs C", price: "$800" },
      { name: "Laptop AB", specs: "Specs A", price: "$1000" },
      { name: "Laptop BAA", specs: "Specs B", price: "$1200" },
      { name: "Laptop CS", specs: "Specs C", price: "$800" },
      { name: "Laptop AD", specs: "Specs A", price: "$1000" },
      { name: "Laptop BF", specs: "Specs B", price: "$1200" },
      { name: "Laptop CW", specs: "Specs C", price: "$800" }
    ];
    var filteredLaptops = laptops.filter(function(laptop) {
      return laptop.name.toLowerCase().includes(searchValue.toLowerCase());
    });
    return filteredLaptops;
  }

  function displaySearchResults(results) {
    $('#searchResults').empty(); 
    results.forEach(function(result) {
      var laptopHTML = '<div class="search-result">';
      laptopHTML += '<div class="laptop-details">';
      laptopHTML += '<img src="/Tampilan Web/image/gambar.jpeg" alt="Laptop Image" class="img-fluid laptop-image">';
      laptopHTML += '<div>';
      laptopHTML += '<p><strong>' + result.name + '</strong></p>';
      laptopHTML += '<p>' + result.specs + '</p>';
      laptopHTML += '<p>' + result.price + '</p>';
      laptopHTML += '</div></div></div>';
      $('#searchResults').append(laptopHTML);
    });
  }
});

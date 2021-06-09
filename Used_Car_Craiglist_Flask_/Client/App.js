function onClickedPredictThePrice() {
    console.log("Predict The price button clicked");
    var manufacturer = document.getElementById("uiManufacturer");
    var condition = document.getElementById("uiCondition");
    var cylinders = document.getElementById("uiCylinders");
    var fuel = document.getElementById("uiFuel");
    var odometer = document.getElementById("uiOdometer");
    var transmission = document.getElementById("uiTransmission");
    var drive = document.getElementById("uiDrive");
    var type = document.getElementById("uiType");
    var age = document.getElementById("uiAge");
    var car_size = document.getElementById("uiCar_size");
    var PredictPrice = document.getElementById("uiPredictThePrice");
  
    var url = "http://127.0.0.1:5000/UCC_predict"; //Use this if you are NOT using nginx which is first 7 tutorials
  
    $.post(url, {
        manufacturer: manufacturer.value,
        condition: condition.value,
        cylinders: cylinders.value,
        fuel: fuel.value,
        odometer: parseFloat(odometer.value),
        transmission: transmission.value,
        drive: drive.value,
        type: type.value,
        age: parseFloat(age.value),
        car_size: car_size.value,
    },function(data, status) {
        console.log(data.predicted_price);
        PredictPrice.innerHTML = "<h2>" + data.predicted_price.toString() + " US Dollar</h2>";
        console.log(status);
    });
  }

function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_manufacturer"; // Use this if you are NOT using nginx which is first 7 tutorials
    $.get(url,function(data, status) {
        console.log("got response for get_manufacturer request");
        if(data) {
            var manufacturer = data.manufacturer;
            var uiManufacturer = document.getElementById("uiManufacturer");
            $('#uiManufacturer').empty();
            for(var i in manufacturer) {
                var opt = new Option(manufacturer[i]);
                $('#uiManufacturer').append(opt);
            }
        }
    });
  }

  {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_condition"; // Use this if you are NOT using nginx which is first 7 tutorials
    $.get(url,function(data, status) {
        console.log("got response for get_condition request");
        if(data) {
            var condition = data.condition;
            var uiCondition = document.getElementById("uiCondition");
            $('#uiCondition').empty();
            for(var i in condition) {
                var opt = new Option(condition[i]);
                $('#uiCondition').append(opt);
            }
        }
    });
  }

  {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_cylinders"; // Use this if you are NOT using nginx which is first 7 tutorials
    $.get(url,function(data, status) {
        console.log("got response for get_cylinders request");
        if(data) {
            var cylinders = data.cylinders;
            var uiCylinders = document.getElementById("uiCylinders");
            $('#uiCylinders').empty();
            for(var i in cylinders) {
                var opt = new Option(cylinders[i]);
                $('#uiCylinders').append(opt);
            }
        }
    });
  }

  {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_fuel"; // Use this if you are NOT using nginx which is first 7 tutorials
    $.get(url,function(data, status) {
        console.log("got response for get_fuel request");
        if(data) {
            var fuel = data.fuel;
            var uiFuel = document.getElementById("uiFuel");
            $('#uiFuel').empty();
            for(var i in fuel) {
                var opt = new Option(fuel[i]);
                $('#uiFuel').append(opt);
            }
        }
    });
  }

  {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_transmission"; // Use this if you are NOT using nginx which is first 7 tutorials
    $.get(url,function(data, status) {
        console.log("got response for get_transmission request");
        if(data) {
            var transmission = data.transmission;
            var uiTransmission = document.getElementById("uiTransmission");
            $('#uiTransmission').empty();
            for(var i in transmission) {
                var opt = new Option(transmission[i]);
                $('#uiTransmission').append(opt);
            }
        }
    });
  }
  
  {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_drive"; // Use this if you are NOT using nginx which is first 7 tutorials
    $.get(url,function(data, status) {
        console.log("got response for get_drive request");
        if(data) {
            var drive = data.drive;
            var uiDrive = document.getElementById("uiDrive");
            $('#uiDrive').empty();
            for(var i in drive) {
                var opt = new Option(drive[i]);
                $('#uiDrive').append(opt);
            }
        }
    });
  }

  {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_type"; // Use this if you are NOT using nginx which is first 7 tutorials
    $.get(url,function(data, status) {
        console.log("got response for get_type request");
        if(data) {
            var type = data.type;
            var uiType = document.getElementById("uiType");
            $('#uiType').empty();
            for(var i in type) {
                var opt = new Option(type[i]);
                $('#uiType').append(opt);
            }
        }
    });
  }

  {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_car_size"; // Use this if you are NOT using nginx which is first 7 tutorials
    $.get(url,function(data, status) {
        console.log("got response for get_car_size request");
        if(data) {
            var car_size = data.car_size;
            var uiCar_size = document.getElementById("uiCar_size");
            $('#uiCar_size').empty();
            for(var i in car_size) {
                var opt = new Option(car_size[i]);
                $('#uiCar_size').append(opt);
            }
        }
    });
  }

  window.onload = onPageLoad;
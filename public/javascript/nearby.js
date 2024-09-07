document
        .getElementById("address-form")
        .addEventListener("submit", function (event) {
          event.preventDefault();

          // Get the user's address (In a real application, you'd send this to the backend to fetch nearby shops)
          const address = document.getElementById("address").value;

          // Example logic to display nearby shops (Replace with actual logic to fetch data based on the address)
          if (address) {
            // Show the shop list and instructions
            const shopList = document.getElementById("shop-list");
            const instructions = document.getElementById("instructions");

            shopList.innerHTML = `
          <li class="bg-gray-50 border rounded-lg p-4">
            <h2 class="text-lg font-semibold text-gray-800">Shop Name 1</h2>
            <p class="text-gray-600">123 Main Street, ${address}</p>
            <p class="text-gray-600">Contact: (123) 456-7890</p>
            <div class="mt-4 space-x-2">
              <button onclick="window.location.href='/appointment'" class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg shadow-lg focus:outline-none focus:ring-2 focus:ring-blue-400">
                Deliver
                </button>
                <button onclick="window.location.href='/appointment'" class="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-lg shadow-lg focus:outline-none focus:ring-2 focus:ring-green-400">
                Picked up
                </button>

            </div>
          </li>
          <li class="bg-gray-50 border rounded-lg p-4">
            <h2 class="text-lg font-semibold text-gray-800">Shop Name 2</h2>
            <p class="text-gray-600">456 Elm Street, ${address}</p>
            <p class="text-gray-600">Contact: (987) 654-3210</p>
            <div class="mt-4 space-x-2">
              <button onclick="window.location.href='/appointment'" class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg shadow-lg focus:outline-none focus:ring-2 focus:ring-blue-400">
            Deliver
            </button>
            <button onclick="window.location.href='/appointment'" class="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-lg shadow-lg focus:outline-none focus:ring-2 focus:ring-green-400">
            Picked up
            </button>

            </div>
          </li>
        `;

            shopList.classList.remove("hidden");
            instructions.classList.remove("hidden");
          }
        });
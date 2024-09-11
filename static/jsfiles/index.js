const category = document.querySelector(".category");
const all_posts = document.querySelector(".all_posts");
const show_post = document.querySelector(".show_post");

let categories = [
  { name: "Home", icon: "<i class='bx bx-home-alt'></i>" },
  { name: "News", icon: "<i class='bx bx-news'></i>" },
  { name: "Sport", icon: "<i class='bx bx-football'></i>" },
  { name: "Business", icon: "<i class='bx bxs-business'></i>" },
  { name: "Innovation", icon: "<i class='bx bx-bulb'></i>" },
  { name: "Culture", icon: "<i class='bx bx-globe'></i>" },
  { name: "Entertainment", icon: "<i class='bx bx-party'></i>" },
  { name: "Travel", icon: "<i class='bx bx-map'></i>" },
];

categories.forEach((each, index) => {
  const href = index === 0 ? "/" : `/${each.name.toLowerCase()}/`;

  category.insertAdjacentHTML(
    "beforeend",
    `
    <li>
      <a
        href="${href}"
        class="flex cursor-pointer items-center gap-2 py-2 px-3 transition-all duration-200 ease-linear hover:bg-indigo-800 lg:pr-6"
      >
        ${each.icon}
        <span
          class="w-0 flex-1 overflow-hidden font-[600] transition-all duration-200 ease-linear group-hover/parent:w-[8rem] lg:w-[8rem]"
        >
          ${each.name}
        </span>
      </a>
    </li>
    `,
  );
});
const modal = document.getElementById("comment-modal");
const openModalButton = document.getElementById("open-comment-modal");
const closeModalButton = document.getElementById("close-modal");

// Open the modal
openModalButton?.addEventListener("click", function () {
  modal.classList.remove("opacity-0", "pointer-events-none", "-z-40");
  modal.classList.add("opacity-100", "z-[1000]");
});

// Close the modal when the close button is clicked
closeModalButton?.addEventListener("click", function () {
  modal.classList.remove("opacity-100", "z-[1000]");
  modal.classList.add("opacity-0", "pointer-events-none", "-z-40");
});

// Close the modal when clicking outside of the modal content
window.addEventListener("click", function (event) {
  if (event.target === modal) {
    modal.classList.remove("opacity-100", "z-[1000]");
    modal.classList.add("opacity-0", "pointer-events-none", "-z-40");
  }
});

const comments = document.querySelectorAll(".posts");
const showMoreButton = document.getElementById("show_more_posts");

console.log(showMoreButton);
let visibleCount = 0;
const increment = 10;

function showPost(count) {
  for (let i = 0; i < comments.length; i++) {
    if (i < count) {
      comments[i].classList.remove("hidden");
    } else {
      comments[i].classList.add("hidden");
    }
  }
  visibleCount = count;
}

function handleShowMorePost() {
  const totalComments = comments.length;
  if (visibleCount < totalComments) {
    const newVisibleCount = Math.min(visibleCount + increment, totalComments);
    showPost(newVisibleCount);
  }

  if (visibleCount >= totalComments) {
    showMoreButton.setAttribute("disabled", true);
  }
}

showPost(increment);

showMoreButton?.addEventListener("click", handleShowMorePost);

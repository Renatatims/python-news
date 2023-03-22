async function newsFormHandler(event) {
  event.preventDefault();

  const title = document.querySelector("#titleInput").value;
  const post_url = document.querySelector("#linkInput").value;

  const response = await fetch(`/api/posts`, {
    method: "POST",
    body: JSON.stringify({
      title,
      post_url,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    document.location.replace("/dashboard");
  } else {
    alert(response.statusText);
  }
}

document
  .querySelector(".news-form")
  .addEventListener("submit", newsFormHandler);

(doc, req) => {
  if (doc) {
    let bold = (req.query.bold) ? '<b>' : '';
    return `<h2> ${doc.user.screen_name}</h2><p>${bold}${doc.text}</p>`;
  } else {
    return `<h2>No document found<>h2/>`;
  }
}

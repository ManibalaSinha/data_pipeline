export async function getServerSideProps() {
  // Replace with your backend API URL
  const res = await fetch("http://localhost:8000/api/jobs");
  const jobs = await res.json();
  return { props: { jobs } };
}

export default function Home({ jobs }) {
  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Data Pipeline Jobs</h1>
      <ul>
        {jobs.map((job) => (
          <li key={job.id}>
            <strong>{job.name}</strong> – Status: {job.status} – Duration: {job.duration}s
          </li>
        ))}
      </ul>
    </div>
  );
}

export async function getServerSideProps() {
  const res = await fetch("http://localhost:8000/api/jobs"); // adjust to your API
  const jobs = await res.json();
  return { props: { jobs } };
}

export default function Home({ jobs }) {
  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Data Pipeline Jobs</h1>
      <ul>
        {jobs.map(job => (
          <li key={job.id}>
            <strong>{job.name}</strong> – Status: {job.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

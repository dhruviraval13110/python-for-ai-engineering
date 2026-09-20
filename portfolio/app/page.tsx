'use client';

import { motion } from 'framer-motion';

const projects = [
  ['Python for AI Engineering', 'A structured Python → Data → AI engineering learning laboratory.', 'Python · NumPy · Pandas · ML', 'https://github.com/dhruviraval13110/python-for-ai-engineering'],
  ['Customer Churn', 'Leakage-safe classification pipeline with preprocessing, evaluation and tests.', 'Python · Pandas · Scikit-learn', 'https://github.com/dhruviraval13110/python-for-ai-engineering/tree/main/projects/customer-churn'],
  ['Sales Analytics', 'Testable transactional data cleaning and reporting pipeline.', 'Python · Pandas · Pytest', 'https://github.com/dhruviraval13110/python-for-ai-engineering/tree/main/projects/sales-analytics'],
];

export default function Home() {
  return <main>
    <nav><b>DR</b><span>Dhruvi Raval</span><a href="#projects">Projects</a><a href="#journey">Journey</a><a href="https://github.com/dhruviraval13110">GitHub ↗</a></nav>
    <section className="hero">
      <motion.div initial={{opacity:0,y:24}} animate={{opacity:1,y:0}} transition={{duration:.7}}>
        <p className="eyebrow">AI / ML ENGINEER IN PROGRESS</p>
        <h1>Building from <span>Python</span> to AI systems.</h1>
        <p className="lede">A technical portfolio documenting practical learning through code, experiments, projects, testing and engineering notes.</p>
        <div className="actions"><a className="primary" href="#projects">Explore projects</a><a className="secondary" href="https://github.com/dhruviraval13110">View GitHub</a></div>
      </motion.div>
    </section>
    <section id="journey" className="section">
      <p className="eyebrow">CURRENT JOURNEY</p><h2>Learn it. Build it. Explain it.</h2>
      <div className="journey">{['Python','NumPy','Pandas','Data Analysis','Statistics','Machine Learning'].map((x,i)=><div className="step" key={x}><small>0{i+1}</small><strong>{x}</strong></div>)}</div>
    </section>
    <section id="projects" className="section">
      <p className="eyebrow">SELECTED WORK</p><h2>Projects with engineering intent.</h2>
      <div className="grid">{projects.map(([title,desc,stack,url])=><motion.a whileHover={{y:-6}} className="card" href={url} key={title}><span>{stack}</span><h3>{title}</h3><p>{desc}</p><b>Open project ↗</b></motion.a>)}</div>
    </section>
    <footer>© {new Date().getFullYear()} Dhruvi Raval · Built with Next.js + TypeScript</footer>
  </main>;
}

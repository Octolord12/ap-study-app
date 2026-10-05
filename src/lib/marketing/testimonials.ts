export interface Testimonial {
  quote: string;
  // First name and last initial is plenty; leave out anything identifying.
  name: string;
  course?: string;
  // The student's real AP score. Only shown when set.
  apScore?: 1 | 2 | 3 | 4 | 5;
}

// Real quotes only. Add one when the student (and a parent, if they are under
// 18) has said you may use it, worded as they wrote it. Don't add a course or an
// AP score unless the student actually told you one. The section on the landing
// page renders nothing while this list is empty, so there is nothing to remove
// later and no invented praise to retract.
export const TESTIMONIALS: Testimonial[] = [
  { quote: "Wait this is actually tuff. I actually might use it later.", name: "Phu Vo" },
];
